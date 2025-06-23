https://langchain-ai.github.io/langgraph/agents/mcp/?h=mcp+int#use-mcp-tools

* run weather-server: `uv run weather-server.py`

* run math-server: `uv run client.py`



'''
## output
Processing request of type ListToolsRequest
Processing request of type CallToolRequest
================================ Human Message =================================

what's (3 + 5) x 12?
================================== Ai Message ==================================
Tool Calls:
  multiply (463b956c-4c22-447e-ad30-016b859ca326)
 Call ID: 463b956c-4c22-447e-ad30-016b859ca326
  Args:
    a: 8
    b: 12
================================= Tool Message =================================
Name: multiply

96.0
================================== Ai Message ==================================

The result of the calculation is: 96.0
================================ Human Message =================================

what is the weather in nyc?
================================== Ai Message ==================================
Tool Calls:
  get_weather (6250de74-a902-4e67-901a-d183b6be3adf)
 Call ID: 6250de74-a902-4e67-901a-d183b6be3adf
  Args:
    location: nyc
================================= Tool Message =================================
Name: get_weather

sunny
================================== Ai Message ==================================

The current weather in NYC is sunny!
'''