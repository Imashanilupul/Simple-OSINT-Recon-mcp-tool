from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import Tool, initialize_agent, AgentType
from tools.wigle_tool import wigle_bssid_lookup
from tools.username_tracker import username_tracker
from tools.image_metadata_tool import extract_image_metadata
from settings import settings

@mcp.tool()
def build_osint_agent():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2, google_api_key=settings.GEMINI_API_KEY)
    
    tools = [
        Tool(name="Wigle Lookup", func=wigle_bssid_lookup, description="Looks up BSSID in Wigle export"),
        Tool(name="Username Tracker", func=username_tracker, description="Finds usernames on popular platforms"),
        Tool(name="Image Metadata Extractor", func=extract_image_metadata, description="Extracts metadata from images")
    ]

    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
