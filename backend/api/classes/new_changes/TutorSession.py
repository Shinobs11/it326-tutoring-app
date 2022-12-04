from classes.new_changes.Class import Class
from classes.new_changes.Review import Review
from classes.new_changes.TutorOrganization import TutorOrganization

class TutorSession():
    # Local Variables
    dateTime: str
    location: str
    avgRating: float # Stores the average of the reviews
    reviews = [] # Array of Reviews NOTE: Will be deleted because info is stored on database
    attendees = [] # Array of Observers NOTE: Will be deleted because info is stored on database

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

    # Add rating to the tutor sesssion
    #NOTE: To add data to the database instead of the local array
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

    # Pushes the update to the tutoring session
    def pushUpdate(self, field, updateMessage):
        # Update the field
        match field:
            case "dateTime":
                self.dateTime = updateMessage
            case "location":
                self.location = updateMessage
        
        # Notify all the users enrolled in the tutor session
        self.notifyAll(updateMessage)
        return True

    # Add a user to the tutoring session
    #NOTE: To add data to the database instead of the local array
    def register(self, user):
        # If the user is a tutor, we want to add it to the Tutor Organization list
        if (user.userType == 0 and (user not in self.theOrganization.getTutors())):
            user.joinTutorOrganization(self.theOrganization)

        # Remove the user from the list of users enrolled in the tutor session
        self.attendees.append(user)

        # Add the session to the user's sessions list
        user.getSessions().append(self)

    # Remove a user from the tutoring session
    #NOTE: To add data to the database instead of the local array
    def unregister(self, user):
        # Remove the user from the list of users enrolled in the tutor session
        self.attendees.remove(user)

        #remove from the user's sessions list
        user.getSessions().remove(self)

    # Send a message to all the user's inbox enrolled in the tutor session
    def notifyAll(self, updateMessage):
        # Send a message to all of the users enrolled in this tutor session
        for user in self.attendees:
            print(user.firstName)
        #         user.update(updateMessage)
        #self.attendees[0].update(updateMessage)
            
        # Getter for class info
    def getClassInfo(self):
        return self.theClass.getClassData()

    # Getter for the list of attendees
    #NOTE: To get data from the database instead of the local array
    def getAttendees(self):
        return self.attendees

    # This returns the average rating
    def getAvgRating(self):
        return self.avgRating

    def getTutorOrganization(self):
        return self.theOrganization

    def compareSessions(self, updateMessage):
        # Go through all the sessions that are apart of this organization
        for sessions in self.theOrganization.getSessions():
            # If the change conflicts with another session, return false
            if (sessions is not self):
                # Check if the dateTime or the location is the same.
                if ( (updateMessage == sessions.dateTime) or (updateMessage == sessions.location)):
                    return False
        return True