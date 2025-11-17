import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

# Define the configuration for the local MCP server
# The "command" should be the absolute path to your server script
server_config = {
    "yt_server": {
        "transport": "stdio",  # Use stdio for local subprocess communication
        "command": "python",   # The executable to run the server
        "args": ["mcp-server/server.py"], # Arguments to the command
    }
}

llm = ChatOllama(
    model="gpt-oss:20b",
    temperature=0,
)

async def run_agent():
    # Initialize the client with the server configuration
    # The client manages the server as a subprocess
    client = MultiServerMCPClient(server_config)
        # Load the tools exposed by the local MCP server
    tools = await client.get_tools()

    # Create a LangChain agent using the loaded tools
    agent = create_agent(llm, tools)

    # Invoke the agent with a task that uses the local tool
    while True:
        # Get user input
        user_input = input("\nUser: ").strip()
        response = await agent.ainvoke(
            {"messages": [{"role": "user", "content": user_input}]}
        )
        print(response)

def main():
    print("Hello from ai-mcp-agent!")
    asyncio.run(run_agent())

if __name__ == "__main__":
    main()
