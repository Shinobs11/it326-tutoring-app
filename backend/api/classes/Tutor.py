from api.classes.User import CUser
from api.models.User import User
from api.models.Tutor import Tutor
from api.models.TutorOrganization import TutorOrganization
from api.models.TutorSession import TutorSession
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
        #If no tutor found, returns True
        if not item:
            return True
        else:
            return False

    def isTutorInOrganization(email, session):
        item = User.objects.get(email_address=email)
        #tutor obj
        item = item.tutor
        #session obj
        ses = TutorSession.objects.get(sessName=session)
        ses = ses.tutorOrgID
        ses = ses.tutOrgID
        org = TutorOrganization.objects.all().filter(tutOrgID=ses,tutor=item)
        #If no tutor found in organization, return True
        if not org:
            return True
        else:
            return False