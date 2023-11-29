from flask import Flask, request
from werkzeug.exceptions import BadRequest
from api import Api

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/myapi', methods=['POST'])
def api():

    try:
        data = request.get_json()
    except BadRequest as exep:
        return {"error": exep.description.split(':')[0]}

    process = {
        'fact': lambda x: Api.factorial(x),
        'fibo': lambda x: Api.fibonacci(x),
        # ...
    }

    ans = dict()
    for key in set(data.keys()).intersection(process.keys()):
        ans[key] = process[key](data[key])    

    return ans

if __name__ == '__main__':
    app.run(debug=True, port=5000)
