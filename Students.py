__author__ = 'verasraul'

import uuid


class Student(object):
    roster = {} #empty dictionary to store accounts

    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName
        self.name = firstName + " " + lastName
        self.id = uuid.uuid4()
        self.roster[self.id] = self.name


    def removeFromRoster(self):
        del self.roster[self.id]


class Grades(object):
    courses = {}

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.courses[key] = value


    def printGrades(self):
        print(self.courses)








