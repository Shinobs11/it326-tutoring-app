from tokenize import Double, String
import User, TutorSession, TutorOrganization

class Tutor(User):
    __tutorID:int
    __rating:Double
    __tutorSubject: String
    __numOfTutOrgs:int
    def __init__(self,nm,UID,paswrd,phnNO,eml,schoolYear,tutorSubject):
        self.tutorID=0#Need some way to initialize ID and check if unique
        self.rating=0
        self.tutorSubject=""
        self.numOfTutOrgs=0
        super.__init__(nm,UID,paswrd,phnNO,eml,schoolYear)
    
    def editAvailability():
        pass

    def joinTutOrg(TutorOrganization):
        pass
    #need class for joining tutor session
