# mcp_client.py
import os
import json
from typing import Dict, Any
from openai import OpenAI
from github_integration import fetch_pr_changes
from notion_client import Client
from dotenv import load_dotenv

class DirectPRAnalyzer:
    def __init__(self):
        load_dotenv()
        
        # Initialize clients
        self.openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.notion = Client(auth=os.getenv("NOTION_API_KEY"))
        self.notion_page_id = os.getenv("NOTION_PAGE_ID")
    
    def analyze_pr(self, repo_owner: str, repo_name: str, pr_number: int):
        """Analyze a GitHub PR and create a Notion page with the review."""
        
        # Step 1: Fetch PR data
        print(f"Fetching PR #{pr_number} from {repo_owner}/{repo_name}")
        pr_data = fetch_pr_changes(repo_owner, repo_name, pr_number)
        
        if not pr_data:
            print("Failed to fetch PR data")
            return
        
        # Step 2: Analyze with OpenAI
        print("Analyzing PR with OpenAI...")
        analysis = self._analyze_with_openai(pr_data)
        
        # Step 3: Create Notion page
        print("Creating Notion page...")
        self._create_notion_page(
            title=f"PR Review: {repo_owner}/{repo_name} #{pr_number}",
            content=analysis
        )
    
    def _analyze_with_openai(self, pr_data: Dict[str, Any]) -> str:
        """Use OpenAI to analyze the PR data."""
        prompt = f"""
        Please analyze this GitHub Pull Request and provide a comprehensive code review:

        PR Data:
        {json.dumps(pr_data, indent=2)}

        Please provide:
        1. Summary of changes
        2. Code quality assessment
        3. Potential issues or bugs
        4. Security considerations
        5. Performance implications
        6. Suggestions for improvement
        7. Overall recommendation (approve, request changes, etc.)

        Format your response in a clear, structured manner.
        """
        
        response = self.openai.chat.completions.create(
            model="gpt-4o",  # or "gpt-4-turbo", "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4000,
            temperature=0.1
        )
        
        return response.choices[0].message.content
    
    def _create_notion_page(self, title: str, content: str):
        """Create a Notion page with the analysis."""
        import json
        with open("test_data.json",'w') as f:
            json.dump({"title":title,"content":content},f)
        try:
            self.notion.pages.create(
                parent={"type": "page_id", "page_id": self.notion_page_id},
                properties={"title": {"title": [{"text": {"content": title}}]}},
                children=[{
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [{
                            "type": "text",
                            "text": {"content": content[:1998]}
                        }]
                    }
                }]
            )
            print(f"✅ Notion page '{title}' created successfully!")
        except Exception as e:
            print(f"❌ Error creating Notion page: {str(e)}")

# Usage
if __name__ == "__main__":
    analyzer = DirectPRAnalyzer()
    
    # Example usage
    analyzer.analyze_pr("3b1b", "manim", 1)