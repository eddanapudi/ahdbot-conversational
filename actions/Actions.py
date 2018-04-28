from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionGreet(Action):
    def name(selfself):
        return 'action_greet'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("hey there! Welcome to EDPI Adoption Agent! How can I help you today?")
        return []

class ActionGoodbye(Action):
    def name(self):
        return 'action_goodbye'

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Bye bye. Have a nice day")
        return []
