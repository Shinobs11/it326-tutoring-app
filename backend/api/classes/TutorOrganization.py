from api.models.TutorOrganization import TutorOrganization
from api.models.TutorOrgManager import TutorOrgManager
import random
from api.models.TutorSession import TutorSession
from django.shortcuts import render, redirect

class CTutorOrganization:
    _tutorOrgID: int
    _numOfSessions: int
    numOfTutors: int

    # Default Constructor
    def __init__(self, manager):
        self._tutorOrgID = manager.tutorOrgManagerID

    def createSession(request):
        TutorSession.objects.create(tutorSessID=DtutorSessID,date=Ddate)
    # Creates a tutor organization object
    
    def getTutorOrg(name):
        return(TutorOrganization.objects.get(tutOrgName=name))
    
    def getOrg(Orgname):
        item = TutorOrganization.objects.all().filter(tutOrgName=Orgname)
        if not item:
            return False
        else:
            return True

    
