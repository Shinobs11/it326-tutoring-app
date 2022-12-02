# The Student File
from classes.User import User

class Student(User):
    # Local Variables
    schoolYear: int
    tutorSessHours: int

    # Constructor
    def __init__(self, firstName:str, lastName:str, ULID:str, password:str, phoneNumber:str, email:str, year:str, major:str):
        super().__init__(firstName, lastName, ULID, password, phoneNumber, email, year, major)

    def rateTutorSession(self, TutorSession):
        pass

