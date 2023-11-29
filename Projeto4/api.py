from flask import Flask, request, abort
from typing import Any

class Api():

    @staticmethod
    def validade_input(value: Any, max_value: int = 1000) -> [int, str]:

        class InputTooBig(ValueError):
            def __init__(self, message='Input exceeds maximum allowed') -> None:
                super().__init__(message)
        
        class InputNegative(ValueError):
            def __init__(self, message="Input can not be negative") -> None:
                super().__init__(message)

        try:
            value = int(value)

            if value > max_value:
                raise(InputTooBig)
            
            elif value < 0:
                raise(InputNegative)
        
            return value, "Value evaluated successfully"

        except Exception as exeption:
            return -1, str(exeption)

    @staticmethod
    def format_output(value: int, description: str) -> dict:
        return {
            "description": f'{description}'.capitalize(), 
            "value": value
        }

    @staticmethod
    def fibonacci(n: int) -> int:
        n, desc = Api.validade_input(n, 100)
        if (n != -1):
            last_two = [0, 1]
            for _ in range(n):
                last_two = last_two[1], last_two[0] + last_two[1]            
            n = last_two[0]

        return Api.format_output(n, desc)

    @staticmethod
    def factorial(n: int) -> int:
        n, desc = Api.validade_input(n, 30)
        if (n != -1):
            factorial = 1
            for i in range(1, n+1):
                factorial *= i
            n = factorial 
        
        return Api.format_output(n, desc)
        


