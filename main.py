import asyncio
import sys
from mcp_client import MCPClient

async def main():
    try:
        # Get command line arguments
        llm_provider = sys.argv[1] if len(sys.argv) > 1 else "anthropic"
        config_path = sys.argv[2] if len(sys.argv) > 2 else "config/servers.json"

        # Validate LLM provider
        if llm_provider not in ["anthropic", "deepseek"]:
            raise ValueError(f"Unsupported LLM provider: {llm_provider}. Available options: anthropic, deepseek")

        print(f"Initializing MCP client with {llm_provider} provider...")
        client = MCPClient(llm_provider)

        print(f"Loading MCP servers from {config_path}...")
        await client.load_mcp_servers(config_path)

        try:
            await client.chat_loop()
        finally:
            await client.cleanup()

    except KeyboardInterrupt:
        print("\nShutting down...")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())