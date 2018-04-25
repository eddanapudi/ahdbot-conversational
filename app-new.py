import requests
from decimal import Decimal
from flask import Flask
from flask import render_template, jsonify, request

from engine import *
import json

app = Flask(__name__)
app.secret_key = '12346'

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    try:
        user_message = request.form["text"]
        print(user_message)
        json_data = {"sender": "default", "message": user_message}
        print(json.dumps(json_data))
        response = requests.post(url="http://localhost:5004/chat/webhook", data=json.dumps(json_data))
        print(response.text)
        s = response.text
        t = s[s.find("[") + 1:s.find("]")]
        return jsonify({"status": "success", "response": t})
    except Exception as e:
        print(e)
        return jsonify({"status": "success", "response": "Sorry I am not trained to do that yet..."})

app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)