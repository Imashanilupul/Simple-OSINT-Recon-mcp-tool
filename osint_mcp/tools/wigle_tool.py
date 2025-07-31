import requests
from settings import settings

@mcp.tool()
def wigle_bssid_lookup(bssid: str) -> str:
    url = "https://api.wigle.net/api/v2/network/search"
    params = {
        "netid": bssid,
        "onlymine": False
    }

    try:
        response = requests.get(url, auth=(settings.WIGLE_API_NAME, settings.WIGLE_API_TOKEN), params=params)
        data = response.json()

        if not data.get("success"):
            return f"❌ Wigle API Error: {data.get('message', 'Unknown error')}"

        if data["totalResults"] == 0:
            return f"❌ No data found for BSSID `{bssid}`."

        result = data["results"][0]

        ssid = result.get("ssid", "N/A")
        lat = result.get("trilat", "N/A")
        lon = result.get("trilong", "N/A")
        last_seen = result.get("lastupdt", "N/A")
        city = result.get("city", "N/A")
        road = result.get("road", "N/A")

        return (
            f"📡 BSSID: {bssid}\n"
            f"🔤 SSID: {ssid}\n"
            f"📍 Location: {lat}, {lon}\n"
            f"🏙️ City: {city}\n"
            f"🛣️ Road: {road}\n"
            f"📅 Last Seen: {last_seen}"
        )

    except Exception as e:
        return f"⚠️ Failed to lookup BSSID: {str(e)}"
