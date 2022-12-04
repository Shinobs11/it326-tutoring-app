# Implementation of a Factory Pattern for User
from classes.new_changes.User import User #NOTE: Only here to show the return type of the function on line 11 (..."-> User"). Should we remove that?
from classes.new_changes.Tutor import Tutor
from classes.new_changes.Student import Student
from classes.new_changes.TutorOrgManager import TutorOrgManager
from classes.new_changes.UserType import UserType



class UserFactory():
    # Create Profile
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
            match userType:
                # If the user wants to create a tutor account, we need to ask which subject they want to teach
                case UserType.TUT.value:
                    #TODO: Update this input to communicate with front end; we want to get this from the user
                    subject = input("What subject would you like to tutor for? ")
                    # Make sure subject is a valid input
                    if (len(subject) > 0):
                        return Tutor(firstName, lastName, username, password, phoneNumber, email, subject, userType)
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
                            return Student(firstName, lastName, username, password, phoneNumber, email, year, major, userType)
                        else:
                            print("Not a valid major. Please try again")
                    else:
                        print("Not a valid year. Please enter in range 1-4")
                
                # If the user wants to create a tutorOrgManger class, we don't ask for any variables so we just return the object
                case UserType.TUT_ORG.value:
                    return TutorOrgManager(firstName, lastName, username, password, phoneNumber, email, userType)
        # If any of the inputs were invalid, we prompt the user to try again NOTE: Temporarily is a print. Should change to something on front end?
        else:
            print("Invalid input. Please try again")

    # Delete Profile
    def deleteUser(self, user: User):
        # Get the table of users from the DB
        # Search for the userID in the table
        # If the user is in the table
            # If user.userType is Tutor
                # call leaveTutorOrganization method (automatically unenrolls from tutor Session as well)
            # Else If user.UserType is Student
                # for sessions in user.getSessions():
                    # sessions.unregister(user)
            # Else If user.UserType is Tutor Org Manager
                # for orgs in user.getOrganizations:
                    # orgs.deleteTutorOrganization(org)
            # Delete the user from the DB table
        pass