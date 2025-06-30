import os
import shutil
import subprocess
from pathlib import Path
from typing import List, Dict, Any
from mcp.server.fastmcp import FastMCP

# Configure the base path - change this to your desired directory
BASE_PATH = Path("/home/anon-labs/Documents/learning/MCP/tutorials/project-1/files/")  # Change this path!

mcp = FastMCP("FileManager")

def _validate_path(path: str) -> Path:
    """Validate that the path is within the allowed base directory."""
    try:
        # Convert to absolute path and resolve any .. or . components
        full_path = (BASE_PATH / path).resolve()
        
        # Check if the resolved path is within BASE_PATH
        if not str(full_path).startswith(str(BASE_PATH.resolve())):
            raise ValueError(f"Path '{path}' is outside the allowed directory")
        
        return full_path
    except Exception as e:
        raise ValueError(f"Invalid path '{path}': {str(e)}")

@mcp.tool()
async def list_directory(path: str = "") -> Dict[str, Any]:
    """List files and directories in the specified path."""
    try:
        full_path = _validate_path(path)
        
        if not full_path.exists():
            return {"error": f"Path does not exist: {path}"}
        
        if not full_path.is_dir():
            return {"error": f"Path is not a directory: {path}"}
        
        items = []
        for item in full_path.iterdir():
            try:
                stat = item.stat()
                items.append({
                    "name": item.name,
                    "type": "directory" if item.is_dir() else "file",
                    "size": stat.st_size,
                    "modified": stat.st_mtime,
                    "path": str(item.relative_to(BASE_PATH))
                })
            except (OSError, PermissionError):
                # Skip items we can't access
                continue
        
        # Sort items: directories first, then files, both alphabetically
        items.sort(key=lambda x: (x["type"] == "file", x["name"].lower()))
        
        return {
            "path": path,
            "items": items,
            "total": len(items)
        }
    
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
async def create_file(path: str, content: str = "") -> Dict[str, Any]:
    """Create a new file with optional content."""
    try:
        full_path = _validate_path(path)
        
        if full_path.exists():
            return {"error": f"File already exists: {path}"}
        
        # Create parent directories if they don't exist
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Create the file
        full_path.write_text(content, encoding='utf-8')
        
        return {
            "success": True,
            "message": f"File created: {path}",
            "size": len(content.encode('utf-8'))
        }
    
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
async def create_directory(path: str) -> Dict[str, Any]:
    """Create a new directory."""
    try:
        full_path = _validate_path(path)
        
        if full_path.exists():
            return {"error": f"Directory already exists: {path}"}
        
        # Create the directory and any necessary parent directories
        full_path.mkdir(parents=True, exist_ok=True)
        
        return {
            "success": True,
            "message": f"Directory created: {path}"
        }
    
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
async def delete_file(path: str) -> Dict[str, Any]:
    """Delete a file."""
    try:
        full_path = _validate_path(path)
        
        if not full_path.exists():
            return {"error": f"File does not exist: {path}"}
        
        if full_path.is_dir():
            return {"error": f"Path is a directory, use delete_directory instead: {path}"}
        
        full_path.unlink()
        
        return {
            "success": True,
            "message": f"File deleted: {path}"
        }
    
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
async def delete_directory(path: str, recursive: bool = False) -> Dict[str, Any]:
    """Delete a directory. Set recursive=True to delete non-empty directories."""
    try:
        full_path = _validate_path(path)
        
        if not full_path.exists():
            return {"error": f"Directory does not exist: {path}"}
        
        if not full_path.is_dir():
            return {"error": f"Path is not a directory: {path}"}
        
        if recursive:
            shutil.rmtree(full_path)
        else:
            try:
                full_path.rmdir()  # Only works on empty directories
            except OSError:
                return {"error": f"Directory is not empty. Use recursive=True to force deletion: {path}"}
        
        return {
            "success": True,
            "message": f"Directory deleted: {path}"
        }
    
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
async def read_file(path: str, max_size: int = 1024*1024) -> Dict[str, Any]:
    """Read the contents of a file. Limited to max_size bytes for safety."""
    try:
        full_path = _validate_path(path)
        
        if not full_path.exists():
            return {"error": f"File does not exist: {path}"}
        
        if full_path.is_dir():
            return {"error": f"Path is a directory: {path}"}
        
        # Check file size
        file_size = full_path.stat().st_size
        if file_size > max_size:
            return {"error": f"File too large ({file_size} bytes). Maximum allowed: {max_size} bytes"}
        
        content = full_path.read_text(encoding='utf-8')
        
        return {
            "success": True,
            "path": path,
            "content": content,
            "size": file_size
        }
    
    except UnicodeDecodeError:
        return {"error": f"File is not a text file or uses unsupported encoding: {path}"}
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
async def write_file(path: str, content: str) -> Dict[str, Any]:
    """Write content to a file (overwrites existing content)."""
    try:
        full_path = _validate_path(path)
        
        # Create parent directories if they don't exist
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Write the file
        full_path.write_text(content, encoding='utf-8')
        
        return {
            "success": True,
            "message": f"File written: {path}",
            "size": len(content.encode('utf-8'))
        }
    
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
async def search_files(pattern: str, path: str = "", case_sensitive: bool = False, file_extensions: List[str] = None) -> Dict[str, Any]:
    """Search for files containing a pattern using grep-like functionality."""
    try:
        search_path = _validate_path(path)
        
        if not search_path.exists():
            return {"error": f"Search path does not exist: {path}"}
        
        results = []
        
        # Build find command to get files to search
        if file_extensions:
            # Create find expression for multiple extensions
            ext_patterns = []
            for ext in file_extensions:
                ext = ext.strip('.')  # Remove leading dot if present
                ext_patterns.extend(["-name", f"*.{ext}"])
            
            if len(ext_patterns) > 2:
                # Multiple extensions: -name "*.ext1" -o -name "*.ext2" ...
                find_args = ["find", str(search_path), "-type", "f", "("]
                for i, pattern in enumerate(ext_patterns):
                    if i > 0 and pattern == "-name":
                        find_args.append("-o")
                    find_args.append(pattern)
                find_args.append(")")
            else:
                find_args = ["find", str(search_path), "-type", "f"] + ext_patterns
        else:
            find_args = ["find", str(search_path), "-type", "f"]
        
        try:
            # Get list of files
            find_result = subprocess.run(find_args, capture_output=True, text=True, timeout=30)
            if find_result.returncode != 0:
                return {"error": f"Find command failed: {find_result.stderr}"}
            
            files = [f.strip() for f in find_result.stdout.split('\n') if f.strip()]
            
            # Search each file with grep
            for file_path in files:
                if not os.path.isfile(file_path):
                    continue
                
                grep_args = ["grep", "-n"]  # -n for line numbers
                if not case_sensitive:
                    grep_args.append("-i")
                
                grep_args.extend([pattern, file_path])
                
                try:
                    grep_result = subprocess.run(grep_args, capture_output=True, text=True, timeout=10)
                    if grep_result.returncode == 0:  # Found matches
                        matches = []
                        for line in grep_result.stdout.strip().split('\n'):
                            if ':' in line:
                                line_num, content = line.split(':', 1)
                                matches.append({
                                    "line_number": int(line_num),
                                    "content": content.strip()
                                })
                        
                        if matches:
                            results.append({
                                "file": str(Path(file_path).relative_to(BASE_PATH)),
                                "matches": matches,
                                "match_count": len(matches)
                            })
                
                except subprocess.TimeoutExpired:
                    continue  # Skip files that take too long to search
                except Exception:
                    continue  # Skip files that cause errors
        
        except subprocess.TimeoutExpired:
            return {"error": "Search timed out"}
        except Exception as e:
            return {"error": f"Search failed: {str(e)}"}
        
        return {
            "success": True,
            "pattern": pattern,
            "search_path": path,
            "results": results,
            "total_files": len(results),
            "total_matches": sum(r["match_count"] for r in results)
        }
    
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
async def move_file(source: str, destination: str) -> Dict[str, Any]:
    """Move or rename a file or directory."""
    try:
        source_path = _validate_path(source)
        dest_path = _validate_path(destination)
        
        if not source_path.exists():
            return {"error": f"Source does not exist: {source}"}
        
        if dest_path.exists():
            return {"error": f"Destination already exists: {destination}"}
        
        # Create parent directory of destination if it doesn't exist
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        shutil.move(str(source_path), str(dest_path))
        
        return {
            "success": True,
            "message": f"Moved {source} to {destination}"
        }
    
    except Exception as e:
        return {"error": str(e)}

@mcp.tool()
async def copy_file(source: str, destination: str) -> Dict[str, Any]:
    """Copy a file or directory."""
    try:
        source_path = _validate_path(source)
        dest_path = _validate_path(destination)
        
        if not source_path.exists():
            return {"error": f"Source does not exist: {source}"}
        
        if dest_path.exists():
            return {"error": f"Destination already exists: {destination}"}
        
        # Create parent directory of destination if it doesn't exist
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        if source_path.is_dir():
            shutil.copytree(str(source_path), str(dest_path))
        else:
            shutil.copy2(str(source_path), str(dest_path))
        
        return {
            "success": True,
            "message": f"Copied {source} to {destination}"
        }
    
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Check if BASE_PATH is configured
    if str(BASE_PATH) == "/path/to/your/allowed/directory":
        print("WARNING: Please configure BASE_PATH at the top of this file!")
        print("Current BASE_PATH:", BASE_PATH)
    
    # Ensure base path exists
    BASE_PATH.mkdir(parents=True, exist_ok=True)
    
    # Use stdio transport for client connection
    mcp.run(transport="stdio")