import requests
from decimal import Decimal
from flask import Flask
from flask import render_template, jsonify, request

from engine import *

app = Flask(__name__)
app.secret_key = '12345'


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/choice', methods=["POST"])
def userChoice():
    print("in user choices")
    print(request.form["text"])
    entities = []
    e = {'entity': request.form["text"]}
    entities.append(e)
    response_text = intent_response_dict[request.form["text"]]
    h_t = define_html_template(response_text, request.form["text"])
    response_text = hg.generateHTML(h_t)

    return jsonify({"status": "success", "response": response_text})


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        if request.form["submit"] == "AM EDPI":
            return render_template("am_edpi.html")
        elif request.form["submit"] == "WM EDPI":
            return render_template("wm_edpi.html")
        else:
            return render_template('home.html')


@app.route('/chat', methods=['POST', 'GET'])
def chat():
    try:
        user_message = request.form["text"]
        #response = requests.get("http://localhost:5000/parse", params={"q": user_message})
        response = requests.get("http://localhost:5005/conversations/default/parse", params={"q": user_message})
        response = response.json()
        print(response)

        #entities = response.get("entities")
        #topresponse = response["topScoringIntent"]
        #intent = topresponse.get("intent")
        #score = topresponse.get("score")
        #if Decimal(score) < 0.50:
        #    print(" ^^^^^^^^^^^^ Low Confidence ^^^^^^^^^^^^", Decimal(score))
        #print(response)
        #print("Intent {}, Entities {}".format(intent, entities))
        #response_text = getBotResponse(intent, entities)

        #print("response_text" + str(response_text))

        return jsonify({"status": "success", "response": response_text})
    except Exception as e:
        print(e)
        return jsonify({"status": "success", "response": "Sorry I am not trained to do that yet..."})


app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)
