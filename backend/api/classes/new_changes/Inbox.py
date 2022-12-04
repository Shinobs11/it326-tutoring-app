from classes.new_changes.Message import Message

class Inbox():
    #TODO: To be changed for database implementation
    messages = []

    def __init__(self):
        pass

    def getMessage(self):
        for message in self.messages:
            print("Message is:", message.text)

    def addMessage(self, message):
        self.messages.append(Message(message))