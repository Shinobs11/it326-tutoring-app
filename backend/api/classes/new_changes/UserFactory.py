# Implementation of a Factory Pattern for User
from classes.User import User #NOTE: Only here to show the return type of the function on line 11 (..."-> User"). Should we remove that?
from classes.Tutor import Tutor
from classes.Student import Student
from classes.TutorOrgManager import TutorOrgManager
from classes.UserType import UserType


class UserFactory():

    def buildUser(firstName:str, lastName:str, username:str, password:str, phoneNumber:str, email:str, year:str, major:str, userType:int) -> User:
        #TODO: FIX THIS SHIT. IF YOU FORGET, PROFESSOR GONNA SEE WE SWORE

        # If the inputs are valid, we create the user based on the userType
        if ( (len(firstName) <= 15) and (len(lastName) <= 15) and 
             (len(firstName) > 0) and (len(lastName) > 0)  and 
             (len(username) > 0) and (len(password) > 0) and 
             (len(email) > 0) and 
             (len(year) > 0) and (len(major) > 0) and
             (len(phoneNumber) == 10 ) and (phoneNumber.isnumeric()) and 
             ("@" in email) and 
             (".com" in email or ".edu" in email)
            ):
            match userType:
                case UserType.TUT.value:
                    return Tutor(firstName, lastName, username, password, phoneNumber, email, year, major)
                case UserType.STU.value:
                    return Student(firstName, lastName, username, password, phoneNumber, email, year, major)
                case UserType.TUT_ORG.value:
                    return TutorOrgManager(firstName, lastName, username, password, phoneNumber, email, year, major)
        # If any of the inputs were invalid, we prompt the user to try again NOTE: Temporarily is a print. Should change to something on front end?
        else:
            print("Invalid input. Please try again")