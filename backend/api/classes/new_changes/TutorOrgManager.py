# The Tutor Organization Manager File
from classes.new_changes.User import User
from classes.new_changes.TutorOrganization import TutorOrganization
from classes.new_changes.TutorSession import TutorSession

class TutorOrgManager(User):
    myOrganizations = [] #NOTE: Will be deleted because info is stored on database

    # Constructor
    def __init__(self, firstName:str, lastName:str, ULID:str, password:str, phoneNumber:str, email:str, userType:int):
        super().__init__(firstName, lastName, ULID, password, phoneNumber, email, userType)

    # Create the Tutor Organization
    #NOTE: To add data to the database instead of the local array
    def createTutorOrganization(self, orgName:str):
        org = TutorOrganization(orgName)
        self.myOrganizations.append(org) #TODO: Add to the database list
        return org #NOTE: Returning the object will not be necessary in DB implementation
    
    # Delete the Tutor Organization
    def deleteTutorOrganization(self, org):
        # Go through all the tutors and have them leave the tutor organization
        for tutor in org.getTutors():
            tutor.leaveTutorOrganization(org)
        
        # Go through all the students in all of the tutor sessions in this organization
        # and remove them from the sessions
        for sessions in org.getSessions():
            for user in sessions.getAttendees():
                sessions.unregister(user)

        self.myOrganizations.remove(org)
    
    # Create a tutoring session
    def createTutorSession(self, className, classType, dateTime, location, orgName):
        sess =  TutorSession(className, classType, dateTime, location, orgName)
        if (sess.compareSessions(dateTime) and sess.compareSessions(location)):
            orgName.addSession(sess)
            return sess
        else:
            print ("Error: Cannot create class. It conflicts with an already existing class")

    # Update a tutoring session
    def updateTutorSession(self, field, updateMessage, tutOrg, tutSess):
        # Make sure it's a valid input
        if (len(updateMessage) > 0):
            return tutOrg.updateSession(field, updateMessage, tutSess)

    # Getter for the list of all the enrolled organizations the tutor is in
    #NOTE: To get data from the database instead of the local array
    def getOrganizations(self):
        return self.myOrganizations

    # Updates the fields of the User's Profile
    #NOTE: To update the User's values in the DB table
    def editProfile(self, firstName, lastName, username, password, phoneNumber, email):
        self.__init__(firstName, lastName, username, password, phoneNumber, email, 2)