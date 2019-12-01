__author__ = 'verasraul'

import uuid

class Student(object):

    def __init__(self, firstname: str, lastname: str):  # Initiate Student instance w/ firstname & lastname arg strings.
        self.first = firstname  # Store 'firstname' argument in 'self.first' var.
        self.last = lastname  # Store 'firstname' argument in 'self.first' var.
        self.id = str(uuid.uuid4())  # Initiate UUID with new Student instance and return it as a string.

    def full_name(self): # Get full name method.
        return self.first + ' ' + self.last  # Return instance firstname & lastname vars combined.

    def removeFromRoster(self):
        del self.roster[self.id]



class Grades(object):

    def __init__(self, grades: int):
        self.instancegrade = []
        self.grade = grades
        self.instancegrade.append(self.grade)

    def add_grade(self, newgrade):
        self.newgrade = newgrade
        self.instancegrade.append(self.newgrade)
        return self.instancegrade

    def get_grades(self):
        return self.instancegrade



class Roster(object):
    class_roster = []

    def __init__(self, name, id, grades):
        self.name = name
        self.id = id
        self.grades = grades
        self.instance_roster = {}

        instanceroster = self.instance_roster
        instanceroster[str(self.name)] = '{}' +self.id
        instanceroster['GRADES'] = self.grades

        Roster.class_roster.append(self.instance_roster)

    def get_student_info(self):
        return (self.instance_roster)



