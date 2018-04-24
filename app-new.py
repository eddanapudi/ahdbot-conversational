import requests
from decimal import Decimal
from flask import Flask
from flask import render_template, jsonify, request

from engine import *
import json

app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/chat', methods=['POST', 'GET'])
def chat():
    try:
        user_message = request.form["text"]
        print(user_message)
        data1 = {'sender': 'default', 'message': user_message}
        response = requests.post(url='http://localhost:5004/chat/webhook', data={'sender': 'default', 'message': user_message})
        #print(response.json())
        #response = response.json()
        print(response.text)
        return jsonify({"status": "success", "response": "This is testing"})
    except Exception as e:
        print(e)
        return jsonify({"status": "success", "response": "Sorry I am not trained to do that yet..."})

app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)