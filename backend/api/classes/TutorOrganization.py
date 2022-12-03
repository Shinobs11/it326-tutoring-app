

class TutorOrganization:
    _tutorOrgID: int
    _numOfSessions: int
    numOfTutors: int

    # Default Constructor
    def __init__(self, manager):
        self._tutorOrgID = manager.tutorOrgManagerID

    # Creates a tutor organization object
    def createTutorOrganization(self, request):
        return TutorOrganization(manager)