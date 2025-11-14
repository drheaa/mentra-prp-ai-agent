from backend.state import GraphState

# Temporary: disable rewrite so Groq issues don't crash the graph.
# This node will simply leave the last_reply unchanged.
def rewrite_node(state: GraphState) -> GraphState:
    return state
