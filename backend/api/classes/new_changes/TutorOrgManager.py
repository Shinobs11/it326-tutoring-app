# The Tutor Organization Manager File
from classes.User import User

class TutorOrgManager(User):
    # Constructor
    def __init__(self, firstName:str, lastName:str, ULID:str, password:str, phoneNumber:str, email:str, year:str, major:str):
        super().__init__(firstName, lastName, ULID, password, phoneNumber, email, year, major)