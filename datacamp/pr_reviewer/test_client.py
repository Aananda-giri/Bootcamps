import asyncio
from mcp.client import Client

async def test_tools():
    async with Client("http://localhost:8000") as client:
        # Test PR fetch
        pr_data = await client.call(
            "fetch_pr",
            repo_owner="your-org",
            repo_name="your-repo",
            pr_number=123
        )
        print("PR Data:", pr_data)

        # Test Notion creation
        notion_result = await client.call(
            "create_notion_page",
            title="Test Review",
            content="Generated from Python client"
        )
        print("Notion Result:", notion_result)

if __name__ == "__main__":
    asyncio.run(test_tools())