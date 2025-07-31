"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP
from agent import build_osint_agent
from tools.wigle_tool import wigle_bssid_lookup
from tools.username_tracker import username_tracker
from tools.image_metadata_tool import extract_image_metadata


 
# Create an MCP server
mcp = FastMCP("OSINT MCP")

@mcp.tool()
def build_agent():
    """
    Build the OSINT agent with the specified tools and LLM.
    """
    return build_osint_agent()

@mcp.tool()
def run_wigle_lookup(bssid: str) -> str:
    """
    Run the Wigle BSSID lookup tool.
    """
    return wigle_bssid_lookup(bssid)

@mcp.tool()
def run_username_tracker(username: str) -> str:
    """
    Run the username tracker tool.
    """
    return username_tracker(username)

@mcp.tool()
def run_image_metadata_extractor(path: str) -> str:
    """
    Run the image metadata extractor tool.
    """
    return extract_image_metadata(path)

if __name__ == "__main__":
    # Start the MCP server
    mcp.run(transport="stdio")


