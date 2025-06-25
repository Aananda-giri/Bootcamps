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
                # Ensure your weather server is running on port 8000
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
            },
            "code_executor": {
                # Your new code executor server running on HTTP
                "url": "http://localhost:8000/message",
                "transport": "streamable_http",
            }
        }
    )
    tools = await client.get_tools()
    agent = create_react_agent(model, tools)

    # Test math functionality
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )
    print("=== MATH RESPONSE ===")
    for m in math_response['messages']:
        m.pretty_print()
    
    # Test weather functionality
    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what is the weather in nyc?"}]}
    )
    print("\n=== WEATHER RESPONSE ===")
    for m in weather_response['messages']:
        m.pretty_print()
    
    # Test code execution functionality
    code_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "Execute this Python code: print('Hello from MCP code executor!'); result = 2 + 3; print(f'2 + 3 = {result}')"}]}
    )
    print("\n=== CODE EXECUTION RESPONSE ===")
    for m in code_response['messages']:
        m.pretty_print()

if __name__ == "__main__":
    asyncio.run(main())