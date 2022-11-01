from abc import ABC#used to create abstract classes. Not needed for this class but
#will be useful when creating user
import ClassResources

class Class:

    def __init__(self,ID,className, type,studentEnrollment):
        self.classID=ID
        self.className=className
        self.type=type
        self.studentEnrollment=studentEnrollment
        #guessing we need to initialize classresources here so "Class" can access materials.
    def getClassInfo(self)



