from classes.Class import Class
from classes.Tutor import Tutor
from classes.TutorOrganization import TutorOrganization

class TutorSession():
    # Local Variables
    dateTime: str
    location: str
    rating: int # Stores the average of the reviews
    reviews = [] # Array of Reviews
    attendees = [] # Array of Observers NOTE: Confirm we are stating Observers, not Students (Same thing, but want to clarify)

    # Objects
    theClass: Class # The Class Object

    
    

    # Constructor
    def __init__(self, className, classType, dateTime, location):
        self.theClass = Class(className, classType)
        self.dateTime = dateTime
        self.location = location
        self.rating = 0 # NOTE: Since we just created the tutor session, it's default value is 0
    
    #NOTE: Ignoring getNumOfTutors, getClassInfo, updateTutorSession, and compareSession. Refer to document for the reasons.

    # Getter for number of attendees
    def getNumOfAttendees(self) -> int:
        return len(self.attendees)

    def rateSession(self, rating):
        pass

    def register():
        pass
    
    def unregister():
        pass

    