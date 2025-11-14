from backend.supabase_client import supabase
from backend.state import GraphState

def faq_node(state: GraphState) -> GraphState:
    user_query = state.messages[-1].content.lower()

    rows = supabase.table("faq").select("question, answer, tags").execute().data

    for row in rows:
        # match question or tag keywords
        if row["question"] and row["question"].lower() in user_query:
            state.last_reply = row["answer"]
            return state

        if row["tags"]:
            if any(tag.lower() in user_query for tag in row["tags"]):
                state.last_reply = row["answer"]
                return state

    state.last_reply = (
        f"Here’s what I found about that:\n\n{answer}\n\n"
        "If you want, I can help you book a coaching session to work on this together."
    )
    return state
