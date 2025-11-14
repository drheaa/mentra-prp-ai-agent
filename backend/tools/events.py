# tools/events.py
import re
from backend.supabase_client import supabase
from backend.state import GraphState, EventInfo

def event_info_node(state: GraphState) -> GraphState:
    text = state.messages[-1].content.lower()

    date_match = re.search(r"(20\d{2}-\d{2}-\d{2})", text)

    # By keyword search
    keyword = None
    for w in ["resume", "linkedin", "mock", "interview", "clinic", "workshop", "day"]:
        if w in text:
            keyword = w
            break

    query = supabase.table("events")

    if date_match:
        query = query.eq("start_time", date_match.group(1))

    if keyword:
        query = query.ilike("title", f"%{keyword}%")

    results = query.select("id, title, start_time, location").execute().data

    if not results:
        state.last_reply = "No matching events found."
        return state

    # attach attendance count
    enriched = []
    for event in results:
        attendance = (
            supabase.table("attendance")
            .select("user_id", count="exact")
            .eq("event_id", event["id"])
            .execute()
        )

        count = attendance.count or 0
        enriched.append(f"{event['title']} — {event['start_time']} — {event['location']} (attended: {count})")

    state.last_reply = "Here are the events:\n" + "\n".join(enriched)
    return state
