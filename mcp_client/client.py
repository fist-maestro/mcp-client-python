import asyncio
import json
from typing import Dict, List, Optional, Any
from .service_manager import ServiceManager
from .config import Config
from .logger import Logger
from .types import Message, Tool, MCPServerConfig

class MCPClient:
    def __init__(self, llm_provider: str = "anthropic"):
        self.logger = Logger()
        self.config = Config()
        self.service_manager = ServiceManager(
            name="mcp-client-cli",
            version="1.0.0",
            llm_provider=llm_provider
        )
        self.city_name_map = {
            "深圳": "Shenzhen",
            "北京": "Beijing",
            "上海": "Shanghai",
            "广州": "Guangzhou",
            "杭州": "Hangzhou",
            "成都": "Chengdu",
            "武汉": "Wuhan",
            "西安": "Xian",
            "南京": "Nanjing",
            "重庆": "Chongqing"
        }

    async def load_mcp_servers(self, config_path: str) -> None:
        try:
            config = self.config.load_config(config_path)
            for server_id, server_config in config.items():
                try:
                    await self.service_manager.add_mcp_server(server_config)
                    print(f"Successfully loaded MCP server: {server_id}")
                except Exception as e:
                    print(f"Failed to load MCP server {server_id}: {e}")
        except Exception as e:
            print(f"Failed to load MCP servers configuration: {e}")
            raise

    async def process_query(self, query: str) -> str:
        messages = [
            {
                "role": "system",
                "content": "你是一个天气助手，可以帮助用户查询天气信息。请使用提供的工具来获取天气数据，并用自然语言回复用户。"
            },
            {
                "role": "user",
                "content": query
            }
        ]

        try:
            response = await self.service_manager.process_query(query, messages)
            return response
        except Exception as e:
            error_msg = f"处理查询时出错：{str(e)}"
            self.logger.log_error(e)
            return error_msg

    async def chat_loop(self) -> None:
        print("\nMCP Client Started!")
        print("Type your queries or 'quit' to exit.")

        while True:
            try:
                query = input("\nQuery: ").strip()
                if query.lower() == "quit":
                    break

                response = await self.process_query(query)
                print(f"\n{response}")
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"\nError: {e}")

    async def cleanup(self) -> None:
        await self.service_manager.cleanup()