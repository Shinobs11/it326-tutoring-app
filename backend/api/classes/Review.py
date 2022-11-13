#Note: Needs to have a composition relationship with tutorSession and tutorOrganization.
#TODO: Add ability for Student to provide rating. Assign rating to class (organization AND session)
class Review():
    _orgRating: int # Numeric value of the rating for the tutor organization
    _orgFeedback: str # String that contains any feedback given by the student for the tutor organization

    _sesRating: int # Numeric value of the rating for the tutor session
    _sesFeedback: str # String that contains any feedback given by the student for the tutor session

    def __init__(self):
        _orgRating, _sesRating = -1
        _orgFeedback, _sesFeedback = "N/A"

    def rateTutorSess(self):
        #Rating for Tutor Session
        while (_sesRating > 5 or _sesRating < 1):
            _sesRating = int(input("Enter rating out of five stars for the Tutor Session: ")) # User input to provide the rating
            if (_sesRating > 5 or _sesRating < 0): # User did not enter a value in range. Restart loop
                print("Rating not within proper range. Please enter a value between 1-5")

        #Feedback for Tutor Session
        _sesFeedback = str(input("Enter any feedback you'd like to add for the Tutor Session: "))

        # TODO: Return values to the Tutor Sess

    def rateTutorOrg(self):
        #Rating for Tutor Org
        while (_orgRating > 5 or _orgRating < 0):
            _orgRating = int(input("Enter rating (0-5: ")) # User input to provide the rating
            if (_orgRating > 5 or _orgRating < 0): # User did not enter a value in range. Restart loop
                print("Rating not within proper range. Please enter a value between 0-5")

        #Feedback for Tutor Org
        _orgFeedback = str(input("Enter any feedback you'd like to add: "))

        # TODO: Return values to the Tutor Org
