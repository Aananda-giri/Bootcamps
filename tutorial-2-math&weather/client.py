from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import asyncio
from langchain_ollama import ChatOllama

#Using Ollama
model = ChatOllama(model="llama3.2") # Or any available Ollama model

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                # Replace with absolute path to your math_server.py file
                "args": ["math-server.py"],
                "transport": "stdio",
            },
            "weather": {
                # Ensure your start your weather server on port 8000
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            }   
        }
    )
    tools = await client.get_tools()
    # agent = create_react_agent(
    #     "anthropic:claude-3-7-sonnet-latest",
    #     tools
    # )
    agent = create_react_agent(model, tools)

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    for m in math_response['messages']:
        m.pretty_print()
    
    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
    )
    for m in weather_response['messages']:
        m.pretty_print()

if __name__ == "__main__":
    asyncio.run(main())
    