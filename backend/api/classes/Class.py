import string
from api.classes.Class import Class

class Class:
    _classID: int
    _className: string
    _classType: string
    _studentsEnrolled: int

    # Default Constructor
    def __init__(self, id, name, type, numStudents):
        self._classID = id
        self._className = name
        self._classType = type
        self._studentsEnrolled = numStudents

    # Gets the Class Info
    def getClassInfo():
        return "string"