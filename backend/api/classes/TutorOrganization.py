from api.models.TutorOrganization import TutorOrganization
from api.models.TutorOrgManager import TutorOrgManager
import random
class CTutorOrganization:
    _tutorOrgID: int
    _numOfSessions: int
    numOfTutors: int

    # Default Constructor
    def __init__(self, manager):
        self._tutorOrgID = manager.tutorOrgManagerID

    # Creates a tutor organization object
    def createTutorOrganization(self, request):
        TOM =TutorOrgManager.objects.filter(pk='4b3f5ea1-debe-47cb-bdfd-5d672604c683')# tutor org manager object
        name=request.POST['Name']
        instance=TutorOrganization.objects.create(tutOrgName=name) 
        pass