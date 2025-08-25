from typing import Dict
from .nlp import (
    SentimentValidator,
    ToxicityValidator,
)

class NLPValidator:
    def __init__(self):
        self.validators = [
            SentimentValidator(),
            ToxicityValidator(),
        ]

    def validate(self, request: Dict) -> bool:
        return all(validator.validate(request) for validator in self.validators)