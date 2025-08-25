from .nlp.intent_classifier import IntentClassifier
from .nlp.semantic_classifier import SemanticClassifier
from .base import ClassificationResult

class NLPClassifier:
    def __init__(self):
        self.classifiers = [
            IntentClassifier(),
            SemanticClassifier()
        ]

    def classify(self, query: str) -> ClassificationResult:
        pass