from typing import Dict, List, Any
from anthropic import Anthropic
from .base import LLMProvider
from ..config import Config

class AnthropicService(LLMProvider):
    def __init__(self, tools: List[Dict[str, Any]]):
        super().__init__(tools)
        config = Config()
        self.client = Anthropic(api_key=config.get("ANTHROPIC")["API_KEY"])
        self.model = config.get("ANTHROPIC")["MODEL"]

    async def process_query(self, query: str, messages: List[Dict[str, Any]]) -> str:
        try:
            response = await self.client.messages.create(
                model=self.model,
                messages=messages,
                tools=self.tools
            )
            return response.content[0].text
        except Exception as e:
            raise Exception(f"Anthropic API error: {str(e)}")