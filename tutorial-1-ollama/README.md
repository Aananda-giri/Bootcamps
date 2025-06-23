https://medium.com/@diwakarkumar_18755/understanding-model-context-protocol-mcp-with-langgraph-and-ollama-a-practical-guide-1aea1c2a9937

* ensure llama3.2 is running: `ollama run llama3.2`

* install langchain-ollama: `uv add langchain-ollama`

* run client: `uv run client_with_ollama.py`

* run server: `uv run string_tools_server.py`

* run datetime server: `uv run datetime_tools_server.py`

* run multi server client: `uv run multi_server_client_ollama.py`



```
## output of client_with_ollama.py
================================ Human Message =================================

Reverse the string 'hello world'
================================== Ai Message ==================================
Tool Calls:
  reverse_string (e717a47e-e8c8-4817-878b-5596a13eee01)
 Call ID: e717a47e-e8c8-4817-878b-5596a13eee01
  Args:
    text: hello world
================================= Tool Message =================================
Name: reverse_string

dlrow olleh
================================== Ai Message ==================================

Reversed the string 'hello world'. The reversed string is: dlrow olleh.
Processing request of type CallToolRequest





================================ Human Message =================================

How many words are in the sentence 'Model Context Protocol is powerful'?
================================== Ai Message ==================================
Tool Calls:
  count_words (4555a0d6-09a0-419e-a134-7608ddd27878)
 Call ID: 4555a0d6-09a0-419e-a134-7608ddd27878
  Args:
    text: Model Context Protocol is powerful
================================= Tool Message =================================
Name: count_words

5
================================== Ai Message ==================================

The output of the `count_words` function indicates that there are 5 words in the given sentence: "Model Context Protocol is powerful". Therefore, the answer to the original user question is:

There are 5 words in the sentence 'Model Context Protocol is powerful'.================================ Human Message =================================

Reverse the string 'hello world'
================================== Ai Message ==================================
Tool Calls:
  reverse_string (e717a47e-e8c8-4817-878b-5596a13eee01)
 Call ID: e717a47e-e8c8-4817-878b-5596a13eee01
  Args:
    text: hello world
================================= Tool Message =================================
Name: reverse_string

dlrow olleh
================================== Ai Message ==================================

Reversed the string 'hello world'. The reversed string is: dlrow olleh.
Processing request of type CallToolRequest





================================ Human Message =================================

How many words are in the sentence 'Model Context Protocol is powerful'?
================================== Ai Message ==================================
Tool Calls:
  count_words (4555a0d6-09a0-419e-a134-7608ddd27878)
 Call ID: 4555a0d6-09a0-419e-a134-7608ddd27878
  Args:
    text: Model Context Protocol is powerful
================================= Tool Message =================================
Name: count_words

5
================================== Ai Message ==================================

The output of the `count_words` function indicates that there are 5 words in the given sentence: "Model Context Protocol is powerful". Therefore, the answer to the original user question is:

There are 5 words in the sentence 'Model Context Protocol is powerful'.
```



```
## output of multi_server_client_ollama.py
================================ Human Message =================================

Reverse the string 'LangGraph and MCP are cool!'
================================== Ai Message ==================================
Tool Calls:
  reverse_string (18034423-64ea-4f7f-a775-4ab380c2cab9)
 Call ID: 18034423-64ea-4f7f-a775-4ab380c2cab9
  Args:
    text: LangGraph and MCP are cool!
================================= Tool Message =================================
Name: reverse_string

!looc era PCM dna hparGgnaL
================================== Ai Message ==================================

The reversed string is: "looc era PCM dan hgaalpG nahlG".
Processing request of type CallToolRequest
================================ Human Message =================================

What is the current date and time?
================================== Ai Message ==================================
Tool Calls:
  current_datetime (b330cd1b-218a-4f18-9bf3-7db157196d0c)
 Call ID: b330cd1b-218a-4f18-9bf3-7db157196d0c
  Args:
================================= Tool Message =================================
Name: current_datetime

2025-06-23 12:25:45
================================== Ai Message ==================================

The current date and time is June 23, 2025, at 12:25 PM.
Processing request of type CallToolRequest
================================ Human Message =================================

How many days until 2025-12-31?
================================== Ai Message ==================================
Tool Calls:
  days_until (18ca816f-d6ff-4ff7-86f8-a7c161bed7f0)
 Call ID: 18ca816f-d6ff-4ff7-86f8-a7c161bed7f0
  Args:
    date_str: 2025-12-31
================================= Tool Message =================================
Name: days_until

190
================================== Ai Message ==================================

The number of days until December 31, 2025 is 190.
```