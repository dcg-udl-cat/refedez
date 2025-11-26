import uuid
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class UvProject:
    path: Path

    def __post_init__(self):
        pass

    @property
    def hash(self) -> str:
        return str(uuid.uuid4())
