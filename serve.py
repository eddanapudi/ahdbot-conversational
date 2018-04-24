from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import json

from rasa_core.channels import HttpInputChannel
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.channel import UserMessage
from rasa_core.channels.direct import CollectingOutputChannel
from rasa_core.channels.rest import HttpInputComponent
from flask import Blueprint, request, jsonify

logger = logging.getLogger(__name__)


class EdpAhdWebBot(HttpInputComponent):
    """A simple web bot that listens on a url and responds."""

    def blueprint(self, on_new_message):
        custom_webhook = Blueprint('custom_webhook', __name__)

        @custom_webhook.route("/status", methods=['GET'])
        def health():
            return jsonify({"status": "ok"})

        @custom_webhook.route("/webhook", methods=['POST'])
        def receive():
            payload = json.loads(request.data)
            sender_id = payload["sender"]
            text = payload["message"]
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(sender_id)
            print(text)
            out = CollectingOutputChannel()
            on_new_message(UserMessage(text, out, sender_id))
            responses = [m for _, m in out.messages]
            return jsonify(responses)

        return custom_webhook

def run(serve_forever=True):
    # path to your NLU model
    interpreter = RasaNLUInterpreter("models/default/current")
    # path to your dialogues models
    agent = Agent.load("models/default/dialogue", interpreter=interpreter)
    # http api endpoint for responses
    input_channel = EdpAhdWebBot()
    if serve_forever:
        agent.handle_channel(HttpInputChannel(5004, "/chat", input_channel))
    return agent

if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="DEBUG")
    run()