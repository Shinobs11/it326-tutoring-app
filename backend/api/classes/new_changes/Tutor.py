# The Tutor File
from classes.User import User
from classes.new_changes.Observer import Observer

class Tutor(User, Observer):
    # Local Variables
    tutorSubject: str
    enrolledOrganizations = [] # Stores the tutor organizations this tutor is in NOTE: Will be deleted because info is stored on database
    enrolledSessions = [] # Stores the session the Tutor is enrolled in NOTE: Will be deleted because info is stored on database

    # Constructor
    def __init__(self, firstName:str, lastName:str, ULID:str, password:str, phoneNumber:str, email:str, subject:str, userType:int):
        super().__init__(firstName, lastName, ULID, password, phoneNumber, email, userType)
        self.tutorSubject = subject

    # Join a tutorOrganization. We get the Tutor Organization from a drop down menu from Front End
    def joinTutorOrganization(self, tutOrg):
        tutOrg.hireTutor(self)
    
    # Tutor can leave the tutor organization
    def leaveTutorOrganization(self, tutOrg):
        # First, we need to leave all the tutoring sessions that are apart of that organization
        for session in self.enrolledSessions:
            if session in tutOrg.getSessions():
                session.unregister(self)

        # Now we leave the organization
        tutOrg.removeTutor(self)

    # Adds the tutor session to the list of sessions the Tutor is apart of
    def joinTutorSession(self, tutSession):
        tutSession.register(self)

    # Leaves the tutoring session
    def leaveTutorSession(self, tutSession):
        if tutSession in self.enrolledSessions:
            tutSession.unregister(self)
        else:
            print("Not enrolled in this tutoring session")

    # Updates the fields of the User's Profile
    #NOTE: To update the User's values in the DB table
    def editProfile(self, firstName, lastName, username, password, phoneNumber, email, subject):
        self.__init__(firstName, lastName, username, password, phoneNumber, email, subject, 0)
    
    # Getter for the list of all the enrolled organizations the tutor is in
    #NOTE: To get data from the database instead of the local array
    def getOrganizations(self):
        return self.enrolledOrganizations

    # Getter for the list of all the enrolled tutor sessions the tutor is in
    #NOTE: To get data from the database instead of the local array
    def getSessions(self):
        return self.enrolledSessions
