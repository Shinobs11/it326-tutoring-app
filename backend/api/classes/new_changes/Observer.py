class Observer():
    # Add message to the user's inbox
    def update(self, message):
        self.inbox.addMessage(message)
        print(id(self.inbox))