#Note: Needs to have a composition relationship with tutorSession and tutorOrganization.
#TODO: Add ability for Student to provide rating. Assign rating to class (organization AND session)
class CReview():
    _orgRating: int # Numeric value of the rating for the tutor organization
    _orgFeedback: str # String that contains any feedback given by the student for the tutor organization

    _sesRating: int # Numeric value of the rating for the tutor session
    _sesFeedback: str # String that contains any feedback given by the student for the tutor session

    def __init__(self):
        _orgFeedback, _sesFeedback = "N/A"

    def checkRating(rating):
        rating = int(rating)
        if (rating <= 5 or rating >= 1):
            return True
        else:
            return False

        # TODO: Return values to the Tutor Sess

