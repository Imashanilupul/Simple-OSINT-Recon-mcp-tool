"""
FastMCP quickstart example.

cd to the `examples/snippets/clients` directory and run:
    uv run server fastmcp_quickstart stdio
"""

from mcp.server.fastmcp import FastMCP

from tools.wigle_tool import wigle_bssid_lookup
from tools.username_tracker import username_tracker
from tools.image_metadata_tool import extract_image_metadata
from tools.ip_scanner import scan_ip_ports


 
# Create an MCP server
mcp = FastMCP("OSINT MCP")



#Done
@mcp.tool()
def run_wigle_lookup(bssid: str) -> str:
    """
    Run the Wigle BSSID lookup tool.
    """
    return wigle_bssid_lookup(bssid)

#Done
@mcp.tool()
def run_username_tracker(username: str) -> str:
    """
    Run the username tracker tool.
    """
    return username_tracker(username)

@mcp.tool()
def run_ip_scanner(ip_address: str, start_port: int, end_port: int) -> str:
    """
    Run the IP scanner tool.
    """
    return scan_ip_ports(ip_address,start_port,end_port)

#under working
@mcp.tool()
def run_image_metadata_extractor(path: str) -> str:
    """
    Run the image metadata extractor tool.
    """
    return extract_image_metadata(path)

if __name__ == "__main__":
    # Start the MCP server
    mcp.run(transport="stdio")


