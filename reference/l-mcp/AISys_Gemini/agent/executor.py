import os
from typing import Dict, Any, List

class ToolExecutor:
    """
    Executes the actual low-level operations.
    Isolated from Decisions.
    """
    
    def execute(self, tool_name: str, params: Dict[str, Any]) -> Any:
        if tool_name == "fs.list":
            return self._fs_list(params.get("path"))
        elif tool_name == "fs.read":
            return self._fs_read(params.get("path"))
        else:
            raise ValueError(f"Unknown tool: {tool_name}")

    def _fs_list(self, path: str) -> List[str]:
        # Safety: in a real L-MCP, this would strict sandbox. 
        # Here we just list provided it exists.
        if not path or not os.path.exists(path):
             raise FileNotFoundError(f"Path not found: {path}")
        return os.listdir(path)

    def _fs_read(self, path: str) -> str:
        if not path or not os.path.exists(path):
             raise FileNotFoundError(f"Path not found: {path}")
        if not os.path.isfile(path):
             raise ValueError(f"Not a file: {path}")
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
