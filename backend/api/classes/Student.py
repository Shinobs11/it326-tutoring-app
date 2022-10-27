from api.classes.User import User

class Student(User):
    __schoolYear:int
    __tutorSessHour:int
    def __init__(self,nm,UID,paswrd,phnNo,eml,schoolYear):
        super().__init__(nm,UID,paswrd,phnNo,eml)
        self.__schoolYear=schoolYear
        self.__tutorSessHour=0
    def rateTutorSession(self,TutorSession):
        rating =-1
        while(rating > 5 or rating < 0):
            rating= input("Enter rating (0-5)")
            if(rating > 5 or rating < 0):
                print("Rating not within proper range. Select again")
            
        TutorSession.rate(rating)
    
    def login(self,UID,paswrd):
        super.login(UID,paswrd)

    def authenticate(self):
        super.authenticate()