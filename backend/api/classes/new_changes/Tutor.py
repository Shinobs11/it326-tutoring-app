# The Tutor File
from classes.User import User
from classes.Observer import Observer

class Tutor(User, Observer):
    # Local Variables
    tutorSubject: str
    enrolledOrganizations = [] #NOTE: Instead of an int, I'm having numOftutOrgs just store the tutor organizations this tutor is in
    enrolledSessions = [] # Stores the session the Tutor is enrolled in

    # Constructor
    def __init__(self, firstName:str, lastName:str, ULID:str, password:str, phoneNumber:str, email:str, subject:str):
        super().__init__(firstName, lastName, ULID, password, phoneNumber, email)
        self.tutorSubject = subject

    # Join a tutorOrganization. We get the Tutor Organization from a drop down menu from Front End
    def joinTutorOrganization(self, tutOrg):
        tutOrg.hireTutor(self)
        self.enrolledOrganizations.append(tutOrg)
    
    # Adds the tutor session to the list of sessions the Tutor is apart of
    def joinTutorSession(self, tutSession):
        self.enrolledSessions.append(tutSession)

    #TODO: Implement Observer pattern? 
