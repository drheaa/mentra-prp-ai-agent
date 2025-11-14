# backend/app.py
from backend.graphstructure import build_graph
from backend.state import GraphState, Message

def main():
    print("Mentra: PRP AI Agent backend. Type 'exit' to quit.\n")

    # Build graph once
    app = build_graph()

    # Initial state
    state = GraphState(
        messages=[],
        last_reply=None,
        intent=None,
        conversation_id=None,
        user_id=None  # optional for now
    )

    while True:
        user_input = input("You: ")

        if user_input.strip().lower() == "exit":
            break

        # Append user message
        state.messages.append(Message(role="user", content=user_input))

        # Run agent
        out = app.invoke(state)

        # LangGraph returns dict → convert to GraphState
        state = GraphState(**out)

        # Print reply
        reply = state.last_reply or "(no reply)"
        print("\nMentra:", reply, "\n")

if __name__ == "__main__":
    main()
