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
    def createTutorOrganization(request):
        TOM =TutorOrgManager.objects.filter(pk='7e5b1e7f-9ca5-499d-804a-e545a0116be5')# tutor org manager object
        name=request.POST['Name']
        instance=TutorOrganization.objects.create(tutOrgName=name) 
        pass