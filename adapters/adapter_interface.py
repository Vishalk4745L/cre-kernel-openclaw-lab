from abc import ABC, abstractmethod
from typing import Dict, Any


class AgentAdapter(ABC):
    """
    Kernel Lab Adapter Interface (v1)

    ⚠️ NOTE:
    - Core Kernel is NOT touched
    - This interface mirrors kernel expectations
    - Future adapters (MCP / A2A / SDK) plug here
    """

    adapter_id: str
    adapter_type: str  # agent | tool | orchestrator

    @abstractmethod
    def capabilities(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def send(self, message: Dict[str, Any]) -> Dict[str, Any]:
        pass

    @abstractmethod
    def health(self) -> Dict[str, Any]:
        pass