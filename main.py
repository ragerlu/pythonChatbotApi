#
# Author: Lucas Rager
# A chatbot api.
# 

from flask import Flask, request
from collections import namedtuple

app = Flask(__name__)

#  Home page
@app.route('/')
def index():
    return f'<h1>Test Home Page.</h1>'

#  Api endpoint
@app.route('/api')
def api():
    user_input = request.args.get('input')
    response = generate_response(user_input)

    json = {
        'input': user_input,
        'response': response.response,
        'accuracy': response.accuracy
    }

    return json

# Tuple for returning responses
Response = namedtuple('Response', 'response accuracy')

def generate_response(user_input: str) -> Response:
    lowercase_input = user_input.lower()

    if lowercase_input == "hello":
        return Response("Hey there!", 1)
    elif lowercase_input == "goodbye":
        return Response("See you later!", 1)
    else:
        return Response("Could not understand.", 0)



if __name__ == '__main__':
    app.run()