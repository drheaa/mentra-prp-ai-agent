# tools/coach_availability.py
import re
from datetime import datetime, timedelta
from backend.supabase_client import supabase
from ..state import GraphState

def coach_availability_node(state: GraphState) -> GraphState:
    if not state.messages:
        state.last_reply = "Ask me which day you want to see availability for."
        return state

    text = state.messages[-1].content.lower()
    date_match = re.search(r"(20\d{2}-\d{2}-\d{2})", text)

    # If no date, just show next few unbooked slots
    if not date_match:
        slots = (
            supabase.table("coach_availability")
            .select("coach_id, start_time, end_time, is_booked")
            .eq("is_booked", False)
            .limit(10)
            .execute()
            .data
        )
    else:
        date_str = date_match.group(1)
        start_iso = f"{date_str}T00:00:00"
        end_iso = f"{date_str}T23:59:59"

        slots = (
            supabase.table("coach_availability")
            .select("coach_id, start_time, end_time, is_booked")
            .eq("is_booked", False)
            .gte("start_time", start_iso)
            .lte("start_time", end_iso)
            .execute()
            .data
        )

    if not slots:
        state.last_reply = "I couldn't find any free coaching slots for that request."
        return state

    # Fetch coach specialisations in one go
    coach_ids = list({s["coach_id"] for s in slots})
    coaches = (
        supabase.table("coaches")
        .select("id, specialisation")
        .in_("id", coach_ids)
        .execute()
        .data
    )
    spec_by_id = {c["id"]: c.get("specialisation") for c in coaches}

    lines = []
    for s in slots:
        coach_id = s["coach_id"]
        spec = spec_by_id.get(coach_id, "coach")
        start = s["start_time"]
        end = s.get("end_time")
        lines.append(f"- {start} → {end or ''} with {spec} (coach_id={coach_id})")

    state.last_reply = (
        "Here are the free coaching slots I found:\n\n"
        + "\n".join(lines)
        + "\n\nTell me which one you want to book."
    )

    return state
