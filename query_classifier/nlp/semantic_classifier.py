from query_classifier2.nlp_classifier import NLPClassifier
from ..base import ClassificationResult

class SemanticClassifier(NLPClassifier):
    def classify(self, query: str) -> ClassificationResult:
        pass