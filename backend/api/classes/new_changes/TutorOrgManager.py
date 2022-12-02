# The Tutor Organization Manager File
from classes.User import User
from classes.TutorOrganization import TutorOrganization
from classes.TutorSession import TutorSession

class TutorOrgManager(User):
    #NOTE: No Local Variables?
    myOrganizations = [] #TODO: Make this a database list

    # Constructor
    def __init__(self, firstName:str, lastName:str, ULID:str, password:str, phoneNumber:str, email:str):
        super().__init__(firstName, lastName, ULID, password, phoneNumber, email)

    # Create the Tutor Organization NOTE: To be determined if needed. Only needed if we can be in charge of multiple organizations
    def createTutorOrganization(self, orgName:str):
        org = TutorOrganization(orgName)
        self.myOrganizations.append(org) #TODO: Add to the database list
        return org

    def createTutorSession(self, className, classType, dateTime, location):
        return TutorSession(className, classType, dateTime, location, self)