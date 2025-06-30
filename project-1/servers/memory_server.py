import duckdb
from datetime import datetime
from mcp.server.fastmcp import FastMCP
import sys
from pathlib import Path
sys.path.append(str(Path.cwd()))
from config.config import settings
mcp = FastMCP("Memory")

class Memory:
    def __init__(self, db_name=settings.MEMORY_PATH):
        self.conn = duckdb.connect(db_name)
    
    def connect(self, drop_table=False):
        # create connect to table
        if drop_table:
            self.conn.execute("DROP TABLE IF EXISTS memory")
        
        # create table only if it does not exist
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS memory(
            content TEXT UNIQUE,
            created_at TIMESTAMP
        )
        """)
    
    def close(self):
        """Terminate the database connection"""
        if self.conn:
            self.conn.close()
    
    def add_memory(self, content, timestamp=None):
        """Add a single memory entry to the database"""
        if timestamp is None:
            timestamp = datetime.now()
        
        self.conn.execute("""
        INSERT OR IGNORE INTO memory VALUES (?, ?)
        """, [content, timestamp])
    
    def add_memories(self, memories):
        """Add multiple memory entries to the database
        
        Args:
            memories: List of tuples (content, timestamp) or list of strings
        """
        data = []
        for memory in memories:
            if isinstance(memory, tuple):
                content, timestamp = memory
            else:
                content = memory
                timestamp = datetime.now()
            data.append((content, timestamp))
        
        self.conn.executemany("""
        INSERT OR IGNORE INTO memory VALUES (?, ?)
        """, data)
    
    def get_memories_by_recency(self, decay_factor=0.001, limit=None):
        """Fetch memories ordered by recency score
        
        Args:
            decay_factor: Controls how quickly memories decay (default: 0.001)
            limit: Maximum number of memories to return (None for all)
        
        Returns:
            List of tuples (content, recency_score, created_at)
        """
        query = """
        SELECT
            content,
            EXP(-(? * DATE_DIFF('second', created_at, NOW()))) AS recency_score,
            created_at
        FROM memory
        ORDER BY recency_score DESC
        """
        
        if limit:
            query += f" LIMIT {limit}"
        
        return self.conn.execute(query, [decay_factor]).fetchall()
    
    def get_all_memories(self):
        """Get all memories from the database"""
        return self.conn.execute("SELECT * FROM memory ORDER BY created_at DESC").fetchall()
    
    def search_memories(self, search_term, decay_factor=0.001):
        """Search for memories containing a specific term, ordered by recency
        
        Args:
            search_term: Text to search for in memory content
            decay_factor: Controls how quickly memories decay (default: 0.001)
        
        Returns:
            List of tuples (content, recency_score, created_at)
        """
        return self.conn.execute("""
        SELECT
            content,
            EXP(-(? * DATE_DIFF('second', created_at, NOW()))) AS recency_score,
            created_at
        FROM memory
        WHERE content LIKE ?
        ORDER BY recency_score DESC
        """, [decay_factor, f"%{search_term}%"]).fetchall()
    
    def delete_memory(self, content):
        """Delete a specific memory by content"""
        self.conn.execute("DELETE FROM memory WHERE content = ?", [content])
    
    def clear_all_memories(self):
        """Clear all memories from the database"""
        self.conn.execute("DELETE FROM memory")
    
    def get_memory_count(self):
        """Get the total number of memories stored"""
        return self.conn.execute("SELECT COUNT(*) FROM memory").fetchone()[0]
    
    def __enter__(self):
        """Context manager entry"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - ensures connection is closed"""
        self.close()

memory = Memory()
memory.connect()

@mcp.tool()
def add_memory(content:str) -> None:
    """Add to memory: facts or other things that might be useful later"""
    memory.add_memory(content)
    return        

@mcp.tool()
def get_memory() -> str:
    """Get text data from memory: facts or other things added previously, that might be useful for performing tasks"""
    memories=""
    # with Memory() as memory:
    # memory.connect(drop_table=False)
    memories = memory.get_all_memories()
    return "\n\n".join([memory[0] for memory in memories])

if __name__ == "__main__":
    mcp.run(transport="stdio")  # Run server via stdio

# # Example usage:
# if __name__ == "__main__":
#     # Using as context manager (recommended)
#     with Memory() as memory:
#         # Initialize the table
#         memory.connect(drop_table=True)
        
#         # Add some memories
#         memory.add_memory("hello world")
#         memory.add_memory("how are you?")
#         memory.add_memory("goodbye", datetime(2025, 6, 25, 9, 0, 0))
        
#         # Or add multiple at once
#         memory.add_memories([
#             "what a beautiful day",
#             ("old memory", datetime(2025, 1, 1, 12, 0, 0))
#         ])
        
#         # Get memories by recency
#         recent_memories = memory.get_memories_by_recency(decay_factor=0.001, limit=5)
#         print("Recent memories:", recent_memories)
        
#         # Search for specific content
#         search_results = memory.search_memories("hello")
#         print("Search results:", search_results)
        
#         # Get all memories
#         all_memories = memory.get_all_memories()
#         print("All memories:", all_memories)
        
#         print(f"Total memories: {memory.get_memory_count()}")