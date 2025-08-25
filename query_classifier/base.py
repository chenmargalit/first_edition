from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class ClassificationResult:
    query_type: str  # 'doctors', 'pharmacies', 'emergency', 'medical_tests'
    confidence_score: float  # 0.0 to 1.0

class BaseClassifier(ABC):
    @abstractmethod
    def classify(self, query: str) -> ClassificationResult:
        pass