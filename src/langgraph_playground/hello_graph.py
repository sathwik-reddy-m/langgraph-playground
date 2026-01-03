from langgraph.graph import StateGraph, START, END

# Define state
class MyState(dict):
    pass

# Define a Node
def hello_node(state: MyState):
    print("Hello from LangGraph!")
    state["message"] = "Hello World"
    return state

# Create the graph
graph = StateGraph(MyState)

# Add node to the graph
graph.add_node("hello", hello_node)

# Define execution flow (edges)
graph.add_edge(START, "hello")
graph.add_edge("hello", END)

# Compile the graph
graph = graph.compile()

# Run the graph
result = graph.invoke({})
