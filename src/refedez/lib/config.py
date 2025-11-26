from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Any, List

from refedez.lib.algorithms.common import FedAlgorithm


class Backend(Enum):
    PYTORCH = "torch"
    NUMPY = "numpy"
    TENSORFLOW = "tensorflow"


@dataclass(frozen=True)
class Client:
    """Configuration for a federated learning client.

    Represents a client participant in the federated learning system, including
    its name and any environment variables required for execution.

    Attributes:
        name: The unique name identifier for the client.
        env_vars: Dictionary of environment variables to set for the client.
    """

    name: str
    env_vars: Dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class Server:
    """Configuration for the federated learning server.

    Represents the central server in the federated learning system, responsible
    for coordinating the training process and aggregating model updates.

    Attributes:
        name: The unique name identifier for the server.
        save_model_path: Optional path where the trained model should be saved.
    """

    name: str
    save_model_path: str | None = None


@dataclass(frozen=True)
class JobConfiguration:
    server: Server
    clients: List[Client]
    refedez_config: str
    to_execute_script_path: str
    num_rounds: int
    model_cls: Any
    type: Backend
    algorithm: FedAlgorithm

    @property
    def num_clients(self) -> int:
        return len(self.clients)
