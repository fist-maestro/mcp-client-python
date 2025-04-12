import os
import json
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.config = {
            "ANTHROPIC": {
                "API_KEY": os.getenv("ANTHROPIC_API_KEY"),
                "MODEL": "claude-3-opus-20240229"
            },
            "DEEPSEEK": {
                "API_KEY": os.getenv("DEEPSEEK_API_KEY"),
                "API_URL": "https://api.deepseek.com",
                "MODEL": "deepseek-chat",
                "MAX_TOKENS": 2000
            }
        }

    def load_config(self, path: str) -> Dict[str, Any]:
        with open(path, 'r') as f:
            return json.load(f)

    def get(self, key: str) -> Any:
        return self.config.get(key)