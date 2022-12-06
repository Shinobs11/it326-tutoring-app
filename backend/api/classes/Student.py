from api.classes.User import CUser
from api.models.Student import Student
from api.models.User import User
from api.models.TutorSession import TutorSession
class CStudent(CUser):
    __schoolYear:int
    __tutorSessHour:int
    def __init__(self,nm,UID,paswrd,phnNo,eml,schoolYear):
        super().__init__(nm,UID,paswrd,phnNo,eml)
        self.__schoolYear=schoolYear
        self.__tutorSessHour=0
    def rateTutorSession(self,TutorSession, rate):
        rating: int
        while(rating > 5 or rating < 0):
            rating = int(input("Enter rating (0-5)"))
            if(rating > 5 or rating < 0):
                print("Rating not within proper range. Select again")
            
        TutorSession.rate(rating)

    #@Override
    def update(self, content):
        pass #Student Update Method

    #Checks if email is registered to a student
    def studentEmailCheck(eml):
        item = User.objects.get(email_address=eml)
        item = Student.objects.filter(user=item)
        #If they are not a student return True
        if not item:
            return True
        else:
            return False

    def isStudentinSession(email, session):
        item = User.objects.get(email_address=email)
        #student obj
        item = item.student
        #session obj
        ses = TutorSession.objects.filter(sessName=session,student=item)
        #If no student found in session, return True
        if not ses:
            return True
        else:
            return False