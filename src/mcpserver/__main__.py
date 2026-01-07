"""
MCP Server - Deep Dive Deployment
Main entry point for the server.
"""

from mcpserver.deployment import mcp


def main():
    """Main entry point."""
    mcp.run()


if __name__ == "__main__":
    main()
