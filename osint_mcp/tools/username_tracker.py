import requests

@mcp.tool()
def username_tracker(username: str) -> str:
    platforms = ["https://github.com/", "https://twitter.com/", "https://instagram.com/"]
    found = []
    for base in platforms:
        url = base + username
        try:
            r = requests.get(url)
            if r.status_code == 200:
                found.append(url)
        except:
            pass
    return "\n".join(found) if found else "No accounts found."
