from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RegexInterpreter
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

logger = logging.getLogger(__name__)


def run_ahdbot_online(input_channel, interpreter,
                          domain_file="edp-ahdbot.yml",
                          training_data_file='story/edpi_stories.md'):
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(), KerasPolicy()],
                  interpreter=interpreter)

    agent.train_online(training_data_file,
                       input_channel=input_channel,
                       max_history=2,
                       batch_size=50,
                       epochs=200,
                       max_training_samples=300)

    return agent


if __name__ == '__main__':
    utils.configure_colored_logging(loglevel="INFO")
    run_ahdbot_online(ConsoleInputChannel(), RegexInterpreter())
