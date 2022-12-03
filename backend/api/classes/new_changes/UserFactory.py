# Implementation of a Factory Pattern for User
from api.classes.User import User #NOTE: Only here to show the return type of the function on line 11 (..."-> User"). Should we remove that?
from api.classes.Tutor import Tutor
from api.classes.Student import Student
from api.classes.TutorOrgManager import TutorOrgManager
from api.classes.UserType import UserType



class UserFactory():

    def buildUser(firstName:str, lastName:str, username:str, password:str, phoneNumber:str, email:str, userType:int) -> User:
        #TODO: FIX THIS SHIT. IF YOU FORGET, PROFESSOR GONNA SEE WE SWORE

        # If the inputs are valid, we create the user based on the userType
        if ( (len(firstName) <= 15) and (len(lastName) <= 15) and 
             (len(firstName) > 0) and (len(lastName) > 0)  and 
             (len(username) > 0) and (len(password) > 0) and 
             (len(email) > 0) and 
             (len(phoneNumber) == 10 ) and (phoneNumber.isnumeric()) and 
             ("@" in email) and 
             (".com" in email or ".edu" in email)
            ):
            # TODO: After User put their basic info, we need to ask the user what kind of account they want to make, and then ask the appropriate questions
            match userType:
                # If the user wants to create a tutor account, we need to ask which subject they want to teach
                case UserType.TUT.value:
                    subject = input("What subject would you like to tutor for? ")
                    # Make sure subject is a valid input
                    if (len(subject) > 0):
                        return Tutor(firstName, lastName, username, password, phoneNumber, email, subject)
                    else:
                        print("Not a valid subject. Please try again")

                # If the user wants to create a student account, we need to ask them to input their Year and Major
                case UserType.STU.value:
                    year = input("What is your Year? (1: Freshman | 2: Sophomore | 3: Junior | 4: Senior | 5: Graduate): ")
                    
                    # Type cast into integer
                    year = int(year)

                    # Make sure year is a valid input
                    if (year >= 1 and year <= 5):
                        major: str = input("What is your major? ")
                        #Make sure major is a valid input
                        if (len(major) > 0):
                            return Student(firstName, lastName, username, password, phoneNumber, email, year, major)
                        else:
                            print("Not a valid major. Please try again")
                    else:
                        print("Not a valid year. Please enter in range 1-4")
                
                # If the user wants to create a tutorOrgManger class, we don't ask for any variables so we just return the object
                case UserType.TUT_ORG.value:
                    return TutorOrgManager(firstName, lastName, username, password, phoneNumber, email)
        # If any of the inputs were invalid, we prompt the user to try again NOTE: Temporarily is a print. Should change to something on front end?
        else:
            print("Invalid input. Please try again")