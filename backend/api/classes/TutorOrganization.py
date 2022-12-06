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
        DclassID=request.POST['classID']
        DtutorSessID=sessionID
        Ddate= request.POST['date']
        Drate= '0'
        TutorSession.objects.create(tutorSessID=DtutorSessID,date=Ddate)
    # Creates a tutor organization object
    
    def getTutorOrg(name):
        if (TutorOrganization.objects.filter(tutOrgName=name)):
            return name