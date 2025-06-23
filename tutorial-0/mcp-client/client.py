import asyncio
from typing import Optional
from contextlib import AsyncExitStack

from mcp import ClientSession, StdioServerParameters
from langgraph.prebuilt import create_react_agent
from mcp.client.stdio import stdio_client
from langchain_core.tools import tool

# from anthropic import Anthropic
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()  # load environment variables from .env

class MCPClient:
    def __init__(self):
        # Initialize session and client objects
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        # self.anthropic = Anthropic()
        self.model = ChatOllama(model="llama3.2")
        self.ollama = None

    async def connect_to_server(self, server_script_path: str):
        """Connect to an MCP server
        
        Args:
            server_script_path: Path to the server script (.py or .js)
        """
        is_python = server_script_path.endswith('.py')
        is_js = server_script_path.endswith('.js')
        if not (is_python or is_js):
            raise ValueError("Server script must be a .py or .js file")
            
        command = "python" if is_python else "node"
        server_params = StdioServerParameters(
            command=command,
            args=[server_script_path],
            env=None
        )
        
        stdio_transport = await self.exit_stack.enter_async_context(stdio_client(server_params))
        self.stdio, self.write = stdio_transport
        self.session = await self.exit_stack.enter_async_context(ClientSession(self.stdio, self.write))
        
        await self.session.initialize()
        
        # List available tools
        response = await self.session.list_tools()
        mcp_tools = response.tools
        
        # Convert MCP tools to LangChain tools
        langchain_tools = []
        for mcp_tool in mcp_tools:
            # Create a tool function for each MCP tool
            def create_tool_function(tool_name, session, tool_description, input_schema):
                @tool(tool_name, description=tool_description, args_schema=input_schema)
                async def mcp_tool_func(**kwargs):
                    """Dynamically created tool function for MCP tool"""
                    print(f"DEBUG: Tool {tool_name} called with kwargs: {kwargs}")
                    result = await session.call_tool(tool_name, kwargs)
                    return result.content
                return mcp_tool_func
            
            # Create the LangChain tool with schema if available
            input_schema = getattr(mcp_tool, 'inputSchema', None)
            langchain_tool = create_tool_function(
                mcp_tool.name, 
                self.session, 
                mcp_tool.description,
                input_schema
            )
            langchain_tools.append(langchain_tool)
        
        self.ollama = create_react_agent(self.model, langchain_tools)
        print("\nConnected to server with tools:", [tool.name for tool in mcp_tools])

    async def process_query(self, query: str) -> str:
        """Process a query using Ollama and available tools"""
        if not self.ollama:
            return "No agent available. Please connect to a server first."
        
        try:
            response = await self.ollama.ainvoke({
                "messages": [{"role": "user", "content": query}]
            })
            
            # Extract the final response from the agent
            final_response = ""
            for message in response.get("messages", []):
                if hasattr(message, 'content'):
                    final_response += message.content + "\n"
                elif isinstance(message, dict) and 'content' in message:
                    final_response += message['content'] + "\n"
            
            return final_response.strip()
            
        except Exception as e:
            return f"Error processing query: {str(e)}"

    async def chat_loop(self):
        """Run an interactive chat loop"""
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")
        
        while True:
            try:
                query = input("\nQuery: ").strip()
                
                if query.lower() == 'quit':
                    break
                    
                response = await self.process_query(query)
                print("\n" + response)
                    
            except Exception as e:
                print(f"\nError: {str(e)}")
    
    async def cleanup(self):
        """Clean up resources"""
        await self.exit_stack.aclose()

async def main():
    import sys
    if len(sys.argv) < 2:
        sys.argv.append(str(Path(Path(__file__).resolve().parent.parent/"weather-server/weather.py").resolve()))
        # print("Usage: python client.py <path_to_server_script>")
        # sys.exit(1)
        
    client = MCPClient()
    try:
        await client.connect_to_server(sys.argv[1])
        await client.chat_loop()
    finally:
        await client.cleanup()

if __name__ == "__main__":
    asyncio.run(main())