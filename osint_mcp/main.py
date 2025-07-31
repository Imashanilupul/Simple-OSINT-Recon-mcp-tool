"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP
from agent import build_osint_agent




# Create an MCP server
mcp = FastMCP(build_osint_agent)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")

