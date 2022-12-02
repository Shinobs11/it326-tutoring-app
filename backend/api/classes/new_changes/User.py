# The User File

class User():
    # Local Variables
    firstName: str
    lastName: str
    username: str
    password: str
    phoneNo: str
    email: str


    # Constructor
    def __init__(self, firstName:str, lastName: str, username:str, password:str, phoneNumber: str, email: str):
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.phoneNo = phoneNumber
        self.email = email
        
    
    # NOTE: Already implemented. Ignoring
    # Calls authenticate to check if the user exists
    def login(self,username,password) -> bool:
        pass

    # NOTE: Already implemented. Ignoring
    # Pull from database and check against the inputted values to check if the user exists
    def authenticate(self,username,passattempt) -> bool:
        pass
    
    #NOTE: This is an abstract method
    def joinTutorSession(self, tutSession):
        pass

    #TODO: Implement Observer pattern