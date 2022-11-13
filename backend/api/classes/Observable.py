class Observable:
    # List of Users
    user_list = []
    
    @AbstractMethod
    def register(self, user):
        pass

    @AbstractMethod
    def unregister(self, user):
        pass
    
    @AbstractMethod
    def notifyAll(): # Implemented in the TutorSession class
        pass
