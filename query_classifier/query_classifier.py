from .simple_classifier import SimpleClassifier
from .nlp_classifier import NLPClassifier
from .base import ClassificationResult

class QueryClassifier:
    def __init__(self):
        self.simple = SimpleClassifier()
        self.nlp = NLPClassifier()

    def classify(self, query: str) -> ClassificationResult:
        pass