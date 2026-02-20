import os
from fastmcp import FastMCP
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP(name="Search_MCP")

API_KEY = os.getenv("TAVILY_KEY")

client = TavilyClient(api_key=API_KEY)


@mcp.tool()
def search(req) -> str:
    """
    When the users provide a request for general information rather than asking for news or weather, search for the request by using this tool
    """
    response = ""
    res = client.search(query=req, topic="general", max_results=1)
    results = res.get("results")
    for result in results:
        for k, v in result.items():
            if k == "content":
                response = v
                break

    return response


if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=3001)