__author__ = 'verasraul'

import uuid


class Student:
    roster = {}

    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName
        self.name = firstName + " " + lastName
        self.id = uuid.uuid4()
        self.roster[self.id] = self.name



    def removeFromRoster(self, name):
        del self.roster[self.id]



newStudent1 = Student("John","Doe")
newStudent2 = Student("Jane", "Doe")

print(Student.roster)

print("Removing Jane Doe from Roster")
newStudent2.removeFromRoster(newStudent2)

print("Printing new roster after removing Jane Doe")
print(Student.roster)


