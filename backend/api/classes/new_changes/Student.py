# The Student File
from api.classes.User import User
#from api.classes.Observer import Observer

class Student(User, Observer):
    # Local Variables
    schoolYear: int
    major: str
    enrolledSessions = []

    # Constructor
    def __init__(self, firstName:str, lastName:str, username:str, password:str, phoneNumber:str, email:str, year:int, major:str):
        super().__init__(firstName, lastName, username, password, phoneNumber, email)
        self.schoolYear = year
        self.major = major   

    def joinTutorSession(self, tutSession):
        self.enrolledSessions.append(tutSession)

    def rateTutorSession(self, tutorSession, rating):
        if (rating >= 1 and rating <= 5):
            tutorSession.addRating(rating)
        else: #TODO: Make it display a message to front end?
            print("Rating is out of range. Please leave a rating between 1-5")

    #TODO: Implement Observer pattern