from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import MessagesState
from langchain_core.messages import HumanMessage, AIMessage

def user_message(state: MessagesState):
    state["messages"].append(
        HumanMessage(content = "Hey, I am Sathwik")
    )
    print("User message added")
    return state

def ai_response(state: MessagesState):
    state["messages"].append(
        AIMessage(content = "Hello Sathwik! Nice to meet you")
    )
    print("\nConversation so far:")
    for msg in state["messages"]:
        print(f"{msg.type}:{msg.content}")

    return state

graph = StateGraph(MessagesState)

graph.add_node("user", user_message)
graph.add_node("ai", ai_response)

graph.add_edge(START, "user")
graph.add_edge("user", "ai")
graph.add_edge("ai", END)

graph = graph.compile()

graph.invoke({"messages":[]})

