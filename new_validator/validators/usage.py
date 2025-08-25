#!/usr/bin/env python3
"""
Simple example usage of the dual validator system
"""

from new_validator.validators.request_validator import RequestValidator


def main():
    # Create the validator
    validator = RequestValidator()

    # Test with a sample request
    sample_request = {
        'username': 'john_doe',
        'email': 'john@example.com',
        'age': 25,
        'comment': 'This is a great product!'
    }

    result = validator.validate(sample_request)

    print(f"Validation result: {result}")
    # print(f"Request data: {sample_request}")


if __name__ == "__main__":
    main()