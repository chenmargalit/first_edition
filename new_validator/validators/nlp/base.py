from abc import ABC, abstractmethod
from typing import Dict

class BaseNLPValidator(ABC):
    @abstractmethod
    def validate(self, request: Dict) -> bool:
        pass