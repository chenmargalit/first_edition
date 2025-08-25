from typing import Dict
from .individual import (
    RequiredFieldsValidator,
    DataTypeValidator,
    StringLengthValidator,
    FormatPatternValidator,
    ValueRangeValidator
)

class BasicInputValidator:
    def __init__(self):
        self.validators = [
            RequiredFieldsValidator(),
            DataTypeValidator(),
            StringLengthValidator(),
            FormatPatternValidator(),
            ValueRangeValidator()
        ]

    def validate(self, request: Dict) -> bool:
        return all(validator.validate(request) for validator in self.validators)