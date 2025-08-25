from dataclasses import dataclass
from typing import Optional


@dataclass
class StorageConfig:
    """Storage connection configuration."""
    host: str = "localhost"
    port: int = 6379
    db: int = 0
    password: Optional[str] = None
