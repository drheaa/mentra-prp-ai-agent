# tools/feedback.py
from datetime import datetime
from backend.supabase_client import supabase
from backend.state import GraphState, Feedback

def feedback_node(state: GraphState) -> GraphState:
    text = state.messages[-1].content

    data = {
        "booking_id": state.booking.id if state.booking else None,
        "author_id": None,
        "advice": text,
        "status": "pending",
        "created_at": datetime.now().isoformat(),
    }

    supabase.table("follow_up_advice").insert(data).execute()

    state.last_reply = "Got it — I'll store this advice and follow up when needed."
    return state
