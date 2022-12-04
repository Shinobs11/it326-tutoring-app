class TutorOrganization():
    # Local Variables
    organizationName: str
    tutorSessions = [] #NOTE: Will be deleted because info is stored on database
    tutors = [] #NOTE: Will be deleted because info is stored on database

    # Constructor
    def __init__(self, name):
        self.organizationName = name

    # Adds a tutor to our tutors array
    #NOTE: To add data to the database instead of the local array
    def hireTutor(self, tutor):
        self.tutors.append(tutor) 
        tutor.enrolledOrganizations.append(self) 

    # Removes a tutor from the tutors array
    #NOTE: To remove data to the database instead of the local array
    def removeTutor(self, tutor):
        self.tutors.remove(tutor)
        tutor.enrolledOrganizations.remove(self)

    # Adds a session to our list of tutoring sessions apart of this organization
    #NOTE: To add data to the database instead of the local array
    def addSession(self, tutSess):
        self.tutorSessions.append(tutSess)
    
    # Removes a tutoring session from the organization
    #NOTE: To remove data to the database instead of the local array
    def removeSession(self, tutSess):
        self.tutorSessions.remove(tutSess)

    # Checks if tutoring session is apart of the organization. If so, pushes
    def updateSession(self, field, updateMessage, tutSess):
        # Check if the tutoring session is in this org's list
        if tutSess in self.tutorSessions:
            # Check that it does not conflict with other sessions in this org
            if (tutSess.compareSessions(updateMessage)):
                return tutSess.pushUpdate(field, updateMessage)
            else:
                print("Session conflicts with another session")
                return False
        else:
            print("Session was not found")
            return False

    # Getter for tutorSessions
    #NOTE: To get data from the database instead of the local array
    def getSessions(self):
        return self.tutorSessions

    # Getter for tutors
    #NOTE: To get data from the database instead of the local array
    def getTutors(self):
        return self.tutors