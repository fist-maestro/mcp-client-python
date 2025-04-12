import logging
from typing import Any, Dict

class Logger:
    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger('mcp-client')

    def log_mcp_response(self, tool_name: str, args: Dict[str, Any], response: Any) -> None:
        self.logger.info(f"Tool {tool_name} response: {response}")

    def log_error(self, error: Exception, context: Dict[str, Any] = None) -> None:
        if context:
            self.logger.error(f"Error: {error}", extra=context)
        else:
            self.logger.error(f"Error: {error}")