# The User File
from classes.new_changes.Inbox import Inbox

class User():
    # Local Variables
    firstName: str
    lastName: str
    username: str
    password: str
    phoneNo: str
    email: str
    userType: int

    # The Inbox Object
    inbox: Inbox

    # Constructor
    def __init__(self, firstName:str, lastName: str, username:str, password:str, phoneNumber: str, email: str, userType: int):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.phoneNo = phoneNumber
        self.email = email
        self.userType = userType
        self.inbox = Inbox()
        
    
    # NOTE: Already implemented. Ignoring
    # Calls authenticate to check if the user exists
    def login(self,username,password) -> bool:
        pass

    # NOTE: Already implemented. Ignoring
    # Pull from database and check against the inputted values to check if the user exists
    def authenticate(self,username,passattempt) -> bool:
        pass
    
    # Search for all the tutor sessions related to a class
    def searchTutorsession(self, classKey):
        # Get the list of all the classes in the DB
        # Search the list for a class key with the passed param "classKey"
        # If the classKey is in the list
            # Get the list of all the sessions that are apart of that class
            # Return that list
        # Else
            # Return a message that states that there are no sessions for that class type
        pass
    
    # Search for a specific Tutor 
    # NOTE: Needs to be clarified here, I am not sure what exactly is the passed param
    def searchTutor(self, className):
        # Get the list of all the classes in the DB
        # Search the list for a class key with the passed param "classKey"
        # If the classKey is in the list
            # Get the list of all the tutors that are apart of that class
            # Return that list
        # Else
            # Return a message that states that there are no tutors for that class type
        pass

    # Edit Profile - Broken into multiple methods
    #NOTE: This is an abstract method
    def editProfile(self, firstName, lastName, username, password, phoneNumber, email):
        pass

    #NOTE: This is an abstract method
    def joinTutorSession(self, tutSession):
        pass

    #NOTE: This is an abstract method
    def leaveTutorSession(self, tutSession):
        pass