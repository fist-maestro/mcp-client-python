from typing import Dict, List, Optional, TypedDict, Literal

class Tool(TypedDict):
    name: str
    description: str
    type: Literal["function"]
    parameters: Dict[str, any]

class MCPServerConfig(TypedDict):
    command: str
    args: List[str]
    env: Optional[Dict[str, str]]

class Message(TypedDict):
    role: Literal["system", "user", "assistant", "tool"]
    content: str
    tool_calls: Optional[List[Dict[str, any]]]
    name: Optional[str]
    tool_call_id: Optional[str]