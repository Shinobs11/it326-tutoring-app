from api.classes.User import CUser
from api.models.User import User
from api.models.Tutor import Tutor
class CTutor(CUser):
    __tutorID:int
    __rating: float
    __tutorSubject: str
    __numOfTutOrgs:int
    def __init__(self,nm,UID,paswrd,phnNO,eml,schoolYear,tutorSubject):
        self.tutorID=0#Need some way to initialize ID and check if unique
        self.rating=0
        self.tutorSubject=""
        self.numOfTutOrgs=0
        super().__init__(nm,UID,paswrd,phnNO,eml)
    
    def editAvailability(self):
        pass

    def joinTutOrg(self, TutorOrganization):
        pass
    #need class for joining tutor session

    #@Override
    def update(self, content):
        pass # Tutor's Update method

    #Checks if email is a tutor
    def tutorEmailCheck(eml):
        item = User.objects.get(email_address=eml)
        item = Tutor.objects.filter(user=item)
        #If empty...
        if not item:
            return True
        else:
            return False