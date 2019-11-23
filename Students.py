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






