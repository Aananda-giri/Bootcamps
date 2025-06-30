* https://medium.com/@sajith_k/creating-an-mcp-server-and-integrating-with-langgraph-5f4fa434a4c7


## MCP Server
* run math server: `uv run servers/math_mcp_server.py`
* run bmi server: `uv run servers/bmi_mcp_server.py`
* run discord server: `uv run servers/discord_mcp_server.py`
* run file manager server: `uv run servers/file_manager_server.py`
* run memory server: `uv run servers/memory_server.py`
* run client: `uv run client.py`

## to switch to ollama from gemini
* comment lines including `ChatGoogleGenerativeAI` and uncomment lines with `ChatOllama`