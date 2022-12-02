class TutorOrganization():
    # Local Variables
    organizationName: str
    tutorSessions = [] #NOTE: Changing numOfSessions to be an array of tutor sessions
    tutors = [] #NOTE: Changing numOfTutors to be an array of tutors

    # Constructor
    def __init__(self, name):
        self.organizationName = name

    # Adds a tutor to our tutors array
    def hireTutor(self, tutor):
        self.tutors.append(tutor)
