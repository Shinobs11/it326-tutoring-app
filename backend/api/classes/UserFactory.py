# Implementation of a Factory Pattern for User
#from classes.new_changes.User import User #NOTE: Only here to show the return type of the function on line 11 (..."-> User"). Should we remove that?
#from classes.new_changes.Tutor import Tutor
#from classes.new_changes.Student import Student
#from classes.new_changes.TutorOrgManager import TutorOrgManager
from api.classes.new_changes.UserType import UserType
from api.models.User import User
from api.models.Student import Student
from api.models.TutorOrgManager import TutorOrgManager
from api.models.Tutor import Tutor


class UserFactory():
    # Create Profile
    
    def buildUser(firstName:str, lastName:str,  email:str, phoneNumber:str, pwrd:str, userType:int):
        instance = User.objects.create(first_name=firstName,last_name=lastName,email_address=email,phone_number=phoneNumber,password=pwrd)
        # If the user wants to create a tutor account, we need to ask which subject they want to teach
        if(UserType.TUT.value==int(userType)):
            tutinstance=Tutor.objects.create()
            instance.tutor=tutinstance
            

        # If the user wants to create a student account, we need to ask them to input their Year and Major
        if(UserType.STU.value==int(userType)):
            stuinstance=Student.objects.create()
            instance.student=stuinstance
            
        
        # If the user wants to create a tutorOrgManger class, we don't ask for any variables so we just return the object
        if(UserType.TUT_ORG.value==int(userType)):
            tutinstance=TutorOrgManager.objects.create()
            instance.tutorOrgManager=tutinstance
            
        instance.save()
    # Delete Profile
    def deleteUser(request):
        User.objects.filter(email_address=request.POST['email']).delete()
