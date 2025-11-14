# tools/kb_search.py
import re
from backend.supabase_client import supabase
from backend.state import GraphState


def _pick_keyword(text: str) -> str:
    # naive keyword extractor: longest word with length >= 4
    words = re.findall(r"[a-zA-Z]{4,}", text.lower())
    if not words:
        return text.strip()
    words.sort(key=len, reverse=True)
    return words[0]

def kb_search_node(state: GraphState) -> GraphState:
    if not state.messages:
        state.last_reply = "Ask me what you want to find in the resources."
        return state

    query_text = state.messages[-1].content
    keyword = _pick_keyword(query_text)

    rows = (
        supabase.table("kb_chunks")
        .select("content, source_type, source_id")
        .ilike("content", f"%{keyword}%")
        .limit(5)
        .execute()
        .data
    )

    if not rows:
        state.last_reply = f"I couldn't find any resources matching '{keyword}'."
        return state

    lines = []
    for row in rows:
        source = row.get("source_type") or "resource"
        snippet = row["content"][:200].replace("\n", " ")
        lines.append(f"- ({source}) {snippet}...")

    state.last_reply = (
        "Here are some resources I think will help:\n\n"
        + "\n".join(lines)
        + "\n\nWant me to summarise one of these or show more material?"
    )
    return state
