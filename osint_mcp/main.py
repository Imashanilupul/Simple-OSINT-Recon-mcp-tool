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
from tools.port_Listner import tcp_port_listener
from tools.phishing_detector_url import check_if_phishing


 
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

#Done
@mcp.tool()
def run_ip_scanner(ip_address: str, start_port: int, end_port: int) -> str:
    """
    Run the IP scanner tool.
    """
    return scan_ip_ports(ip_address,start_port,end_port)

#Done
@mcp.tool()
def run_tcp_port_listener(port: int, host: str,buffer_size:int) -> str:
    """
    Run the TCP port listener tool.
    """
    return tcp_port_listener(port, host, buffer_size)

@mcp.tool()
async def run_phishing_detector(url: str) -> str:
    """
    Run the phishing detector tool.
    """
    result = await check_if_phishing(url)
    return result

#under working
@mcp.tool()
def run_image_metadata_extractor(image: bytes) -> str:
    """
    Run the image metadata extractor tool.
    """
    return extract_image_metadata(image)

if __name__ == "__main__":
    # Start the MCP server
    mcp.run(transport="stdio")


