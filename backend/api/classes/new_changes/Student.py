# The Student File
from classes.User import User
from classes.new_changes.Observer import Observer

class Student(User, Observer):
    # Local Variables
    schoolYear: int
    major: str
    enrolledSessions = [] #NOTE: Will be deleted because info is stored on database

    # Constructor
    def __init__(self, firstName:str, lastName:str, username:str, password:str, phoneNumber:str, email:str, year:int, major:str, userType:int):
        super().__init__(firstName, lastName, username, password, phoneNumber, email, userType)
        self.schoolYear = year
        self.major = major

    # Register for Session
    #NOTE: To add data to the database instead of the local array
    def joinTutorSession(self, tutSession):
        tutSession.register(self)

    # Unenroll for Session
    #NOTE: To remove data to the database instead of the local array
    def leaveTutorSession(self, tutSession):
        if tutSession in self.enrolledSessions:
            tutSession.unregister(self)
        else:
            print("Not enrolled in this tutoring session")

    # Rate Tutor Session
    def rateTutorSession(self, tutorSession, rating):
        if (rating >= 1 and rating <= 5):
            tutorSession.addRating(rating)
        else: #TODO: Make it display a message to front end?
            print("Rating is out of range. Please leave a rating between 1-5")

     # Updates the fields of the User's Profile
    def editProfile(self, firstName, lastName, username, password, phoneNumber, email, year, major):
        self.__init__(firstName, lastName, username, password, phoneNumber, email, year, major, 1)

    # Getter for the list of all the enrolled tutor sessions the tutor is in
    #NOTE: To get data from the database instead of the local array
    def getSessions(self):
        return self.enrolledSessions

   