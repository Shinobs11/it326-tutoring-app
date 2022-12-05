from api.models.TutorOrganization import TutorOrganization
from api.models.TutorOrgManager import TutorOrgManager
import random
from api.models.TutorSession import TutorSession
class CTutorOrganization:
    _tutorOrgID: int
    _numOfSessions: int
    numOfTutors: int

    # Default Constructor
    def __init__(self, manager):
        self._tutorOrgID = manager.tutorOrgManagerID

    def createSession(request,sesID):
        
        DtutorSessID=sesID
        Ddate= request.POST['date']
        SesName=request.POST['SessionName']
        loca=request.POST['location']
        instance=TutorSession.objects.create(tutorSessID=DtutorSessID,date=Ddate,sessName=SesName,location=loca)
        
        TOinstance=TutorOrganization.objects.get(tutOrgName=request.POST['TutorOrgName'])
        TOinstance.tutorSessID=instance
        TOinstance.save()
        
    # Creates a tutor organization object
    