from api.classes.Class import Class
from api.classes.Review import Review
from api.classes.TutorOrganization import TutorOrganization

class TutorSession():
    # Local Variables
    dateTime: str
    location: str
    avgRating: float # Stores the average of the reviews
    reviews = [] # Array of Reviews
    attendees = [] # Array of Observers NOTE: This is an array of students enrolled (maybe tutors?)

    # Objects
    theClass: Class # The Class Object
    theOrganization: TutorOrganization # Stores which organization this session is apart of

    # Constructor
    def __init__(self, className, classType, dateTime, location, tutorOrganization):
        self.theClass = Class(className, classType)
        self.dateTime = dateTime
        self.location = location
        self.theOrganization = tutorOrganization
        self.avgRating = 0 # NOTE: Since we just created the tutor session, it's default value is 0
    
    #NOTE: Ignoring getNumOfTutors, updateTutorSession, and compareSession. Refer to document for the reasons.

    # Getter for class info
    def getClassInfo(self):
        return self.theClass.getClassData()

    # Getter for number of attendees
    def getNumOfAttendees(self) -> int:
        return len(self.attendees)

    # Updates the class info for the Tutor Session
    #TODO: Call notify here to let all the tutors/students know
    def updateSession(self, data:str):
        # Make sure it's a valid input
        if (len(data) > 0):
            self.theClass.updateClassData(data)

    def addRating(self, rating: int):
        theRating = Review(rating)

        # Add the review to our reviews list
        self.reviews.append(theRating)


        # Calculates the average rating
        if (len(self.reviews) >= 2):
            newRating = 0.0
            for review in self.reviews:
                newRating += review.rating
            newRating = newRating / len(self.reviews)
            self.avgRating = newRating
        else:
            self.avgRating += rating