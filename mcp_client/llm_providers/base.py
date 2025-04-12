from abc import ABC, abstractmethod
from typing import Dict, List, Any

class LLMProvider(ABC):
    def __init__(self, tools: List[Dict[str, Any]]):
        self.tools = tools

    @abstractmethod
    async def process_query(self, query: str, messages: List[Dict[str, Any]]) -> str:
        pass