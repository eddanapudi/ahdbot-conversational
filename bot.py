from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels import HttpInputChannel
from rasa_core.channels.facebook import FacebookInput
import logging

logger = logging.getLogger(__name__)

def run(serve_forever=True):
    # create rasa NLU interpreter
    interpreter = RasaNLUInterpreter("models/default/current")
    agent = Agent.load("models/dialogue", interpreter=interpreter)

    input_channel = FacebookInput(
        fb_verify="your_fb_verify_token",  # you need tell facebook this token, to confirm your URL
        fb_secret="your_app_secret",  # your app secret
        fb_tokens={"your_page_id": "your_page_token"},   # page ids + tokens you subscribed to
        debug_mode=True    # enable debug mode for underlying fb library
    )

    if serve_forever:
        agent.handle_channel(HttpInputChannel(5004, "/app", input_channel))
    return agent

if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="DEBUG")
    run()