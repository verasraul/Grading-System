__author__ = 'verasraul'

import uuid


class Student:


    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName
        self.name = firstName + " " + lastName
        self.id = uuid.uuid4()
        #print(self.name)
        #print(self.id)

    def newPupil(self, name):
        pass



newstudent1 = Student("Raul", "Veras")
newstedent2 = Student("Chris","Bonifacio")

