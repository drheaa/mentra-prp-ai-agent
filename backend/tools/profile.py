from backend.supabase_client import supabase
from backend.state import GraphState

def profile_node(state: GraphState) -> GraphState:
    if not state.user_id:
        state.last_reply = "I don't know which user this is. Make sure you're logged in."
        return state

    rows = (
        supabase.table("profiles")
        .select("email, full_name, role")
        .eq("id", state.user_id)
        .execute()
        .data
    )

    if not rows:
        state.last_reply = "I couldn't find your profile in the system."
        return state

    profile = rows[0]
    name = profile.get("full_name") or "Student"
    email = profile.get("email") or "not set"
    role = profile.get("role") or "unknown"

    state.last_reply = (
        f"Here's what I know about you:\n"
        f"- Name: {name}\n"
        f"- Email: {email}\n"
        f"- Role: {role}"
    )
    return state
