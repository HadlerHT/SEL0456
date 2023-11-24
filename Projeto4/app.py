from flask import Flask, request, abort
from typing import Any
from icecream import ic

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/myapi', methods=['POST'])
def api():

    def validade_input(value: Any, maxValue: int = 1000) -> int | None:

        class InputTooBig(ValueError):
            def __init__(self, message='Input Exceeds Maximum Allowed') -> None:
                super().__init__(message)
        
        class InputNegative(ValueError):
            def __init__(self, message="Input Can't be Negative") -> None:
                super().__init__(message)

        try:
            value = int(value)

            if value > maxValue:
                raise(InputTooBig)
            elif value < 0:
                raise(InputNegative)
        
            return value

        except Exception as e:
            abort(400, str(e))

    def fibonacci(n: int) -> int:
        n = validade_input(n, 100)
        lastTwo = [1, 1]
        for _ in range(n - 2):
            lastTwo = lastTwo[1], lastTwo[0] + lastTwo[1]
        return lastTwo[1]

    def factorial(n: int) -> int:
        n = validade_input(n, 30)
        ans = 1
        for i in range(1, n+1):
            ans *= i
        return ans 

    data = request.get_json()
    process = {
        'fact': lambda x: factorial(x),
        'fibo': lambda x: fibonacci(x)
    }

    ans = dict()
    for key in set(data.keys()).intersection(process.keys()):
        ans[key] = process[key](data[key])

    return ans

if __name__ == '__main__':
    app.run(debug=True, port=5000)
