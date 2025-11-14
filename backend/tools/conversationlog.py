# tools/conversation_log.py
from datetime import datetime
from backend.supabase_client import supabase
from backend.state import GraphState

ROLE_TO_SENDER_TYPE = {
    "user": "user",
    "assistant": "assistant",
    "system": "system",
}


def conversation_log_node(state: GraphState) -> GraphState:
    if not state.messages:
        return state

    last_msg = state.messages[-1]

    # 1) Ensure conversation exists
    if not state.conversation_id:
        # simple title: first 80 chars of first user message
        title = last_msg.content[:80] if last_msg.role == "user" else "PRP AI Session"
        conv = (
            supabase.table("conversations")
            .insert(
                {
                    "user_id": state.user_id,
                    "title": title,
                    "created_at": datetime.now().isoformat(),
                }
            )
            .execute()
            .data[0]
        )
        state.conversation_id = conv["id"]

    # 2) Insert message row
    sender_type = ROLE_TO_SENDER_TYPE.get(last_msg.role, "system")

    payload = {
        "conversation_id": state.conversation_id,
        "sender_id": state.user_id if last_msg.role == "user" else None,
        "sender_type": sender_type,
        "content": last_msg.content,
        "created_at": datetime.now().isoformat(),
    }

    supabase.table("messages").insert(payload).execute()

    return state
