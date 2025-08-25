from .simple.keyword_classifier import KeywordClassifier
from .simple.pattern_classifier import PatternClassifier
from .base import ClassificationResult

class SimpleClassifier:
    def __init__(self):
        self.classifiers = [
            KeywordClassifier(),
            PatternClassifier()
        ]

    def classify(self, query: str) -> ClassificationResult:
        pass