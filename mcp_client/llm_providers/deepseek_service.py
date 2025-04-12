from typing import Dict, List, Any
import openai
from .base import LLMProvider
from ..config import Config

class DeepSeekService(LLMProvider):
    def __init__(self, tools: List[Dict[str, Any]]):
        super().__init__(tools)
        config = Config()
        self.client = openai.Client(
            base_url=config.get("DEEPSEEK")["API_URL"],
            api_key=config.get("DEEPSEEK")["API_KEY"]
        )
        self.config = config.get("DEEPSEEK")

    async def process_query(self, query: str, messages: List[Dict[str, Any]]) -> str:
        try:
            response = await self.client.chat.completions.create(
                model=self.config["MODEL"],
                messages=messages,
                tools=self.tools,
                temperature=0.7,
                max_tokens=self.config["MAX_TOKENS"]
            )
            return response.choices[0].message.content or ""
        except Exception as e:
            raise Exception(f"DeepSeek API error: {str(e)}")