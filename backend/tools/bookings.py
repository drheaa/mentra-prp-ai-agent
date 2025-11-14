# tools/bookings.py
import re
from datetime import datetime
from backend.supabase_client import supabase
from backend.state import GraphState, Booking

def booking_node(state: GraphState) -> GraphState:
    text = state.messages[-1].content

    # parse date + time
    date_match = re.search(r"(20\d{2}-\d{2}-\d{2})", text)
    time_match = re.search(r"(\d{1,2}:\d{2})", text)
    topic_match = re.search(r"(?:about|for) ([a-zA-Z ]+)", text)

    if not date_match or not time_match:
        state.last_reply = "Give me a date (YYYY-MM-DD) and time (HH:MM) to book a coaching session."
        return state

    date = date_match.group(1)
    time = time_match.group(1)
    topic = topic_match.group(1).strip() if topic_match else None

    # 1) Find an available coach for that time
    avail = (
        supabase.table("coach_availability")
        .select("coach_id")
        .eq("start_time", time)
        .eq("is_booked", False)
        .execute()
        .data
    )

    if not avail:
        state.last_reply = "No coaches available at that time. Try another slot."
        return state

    coach_id = avail[0]["coach_id"]

    # 2) Create booking
    booking = {
        "student_id": state.messages[-1].sender_id if hasattr(state.messages[-1], "sender_id") else None,
        "coach_id": coach_id,
        "session_date": date,
        "start_time": time,
        "topic": topic,
        "status": "scheduled",
    }

    inserted = supabase.table("bookings").insert(booking).execute().data[0]

    # 3) Mark slot as booked
    supabase.table("coach_availability").update({"is_booked": True}) \
        .eq("coach_id", coach_id).eq("start_time", time).execute()

    state.last_reply = (
        f"Your coaching session is booked!\n"
        f"Date: {date}\n"
        f"Time: {time}\n"
        f"Coach: {coach_id}\n"
        f"Topic: {topic}"
        "If you need to reschedule or cancel, just let me know."
    )
    return state
