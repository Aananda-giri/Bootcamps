# LangGraph Tutorials

- langchain: easily create custom chains.
- lacked a method for easily introducing cycles into these chains (langchain graphs are Directed Acyclic graphs)
- LangGraphs: LLMS in for loop: Called agents
- e.g. if retrieval fails or the quality of results is not good enough then, it makes sense to make a second retrival attempt with different query (which is llm in loop)

Somple loop:

1. Call llm and determine either
   a) what action to take
   a) what response to give to user

2. Take actions, and pass back to step 1

## StateGraph:

- Class that represents the graph
- we initialize thtis class by passing State
- qstate is dictionary (key-value store) that is updated over time.
- state is updated by nodes of the graph (which either update value of attribute or creating new attribute)
-

- we can specify which attributes to oberride

```
from langgraph.graph import StateGraph
from typing import TypedDict, List, Annotated
import Operator


class State(TypedDict):
    input: str
    all_actions: Annotated[List[str], operator.add]


graph = StateGraph(State)
```

- adding nodes to graph

```
graph.add_node("model", model)
graph.add_node("tools", tool_executor)
```

- special end node
  `from langgraph.graph import END`

## Types of Edges

- Starting Edge: First one to be called when input is passed to the graph

- Normal edges: one node should ALWAYS be called after another.
  `graph.add_edge("tools", "model")`

- Conditional Edges:
  - function (often powered by an LLM) is used to determine which node to go to first.
  - To create conditional edge, we need to pass:
    - The upstream node: the output of this node will be looked at to determine what to do next
    - A function: this will be called to determine which node to call next. It should return a string
    - A mapping: this mapping will be used to map the output of the function in (2) to another node. The keys should be possible values that the function in (2) could return. The values should be names of nodes to go to if that value is returned.
- Compile:
  - After defining the graph, we compile it into runnable
  - `app = graph.compile()`

# Reference

- [video tutorial](https://www.youtube.com/watch?v=5h-JBkySK34&list=PLfaIDFEXuae16n2TWUkKq5PgJ0w6Pkwtg)

## video-2: Agent Executor from scratch

# REferences

- [langchain docs](https://python.langchain.com/docs/how_to/#agents)
- [blog](https://blog.langchain.dev/langgraph/)
- [python repo](https://github.com/langchain-ai/langgraph/tree/main?ref=blog.langchain.dev)
