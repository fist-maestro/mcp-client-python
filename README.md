# MCP Client Python

Python implementation of the Model Context Protocol (MCP) client.

## Features

- Support for multiple LLM providers (Anthropic, DeepSeek)
- Dynamic tool loading from MCP servers
- Configurable server connections
- Chat interface with tool execution capabilities

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from mcp_client import MCPClient

# Initialize client with desired LLM provider
client = MCPClient(llm_provider="anthropic")

# Load MCP servers from config
await client.load_mcp_servers("config/servers.json")

# Start chat loop
await client.chat_loop()
```

## Configuration

Create a `.env` file with your API keys:

```env
ANTHROPIC_API_KEY=your_anthropic_key
DEEPSEEK_API_KEY=your_deepseek_key
```

## License

MIT