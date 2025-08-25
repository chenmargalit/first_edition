
from typing import Dict
from .basic_input import BasicInputValidator
from .nlp_validator import NLPValidator

class RequestValidator:
    def __init__(self):
        self.basic = BasicInputValidator()
        self.nlp = NLPValidator()

    def validate(self, request: Dict) -> bool:
        return (
            self.basic.validate(request) and
            self.nlp.validate(request)
        )