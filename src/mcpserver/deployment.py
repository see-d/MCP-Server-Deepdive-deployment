from mcp.server.fastmcp import FastMCP

# Create the MCP server instance
mcp = FastMCP("Deployment")

# Define a simple tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two integers.
    
    Args:
        a: First integer
        b: Second integer
        
    Returns:
        Sum of a and b
    """
    return a + b
