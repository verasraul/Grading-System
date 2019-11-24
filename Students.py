__author__ = 'verasraul'

import uuid


class Student(object):
    #roster = {} #empty dictionary to store students

    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName
        self.name = firstName + " " + lastName
        self.id = uuid.uuid4()
        #self.roster = {}
        #self.roster[self.id] = self.name

    #def addToRoster(self, id, new_student):
        #students =
        #self.name = new_student
        #self.roster[self.id] = self.name

    def removeFromRoster(self):
        del self.roster[self.id]



class Grades(Student):
    #courses = {}

    def __init__(self, **kwargs):
        self.courses = {}
        for key, value in kwargs.items():
            self.courses[key] = value

    def printGrades(self):
        print(self.courses)



class Roster(Student):
    def __init__(self, userID, userName, grades):
        self.userID = self.Student.id
        self.userName = userName
        self.grades = self.grades


    def addToRoster(self, userName, userID, **kwargs):
        all_students = {}
        all_students[userName] = {}
        all_students[userName] = {'ID': userID,
                                'Grades': Grades}
        return all_students







print('created new Student instance in newStudent variable')
newStudent1 = Student

print('creating 3 new Jane Doe instances from Student class')
newStudent2 = Student('Jane', 'Doe')
newStudent3 = Student('John', 'Doe')
newStudent4 = Student('Jim', 'Doe')

print('printing new student instance name and ID')
print(newStudent2.name, newStudent2.id)
print(newStudent3.name, newStudent3.id)
print(newStudent4.name, newStudent4.id)

studentGrades = Grades(math = 80, science = 95, history = 75)
studentGrades.printGrades()

print('converting results to dictionary')
print('...')
print(Roster.addToRoster(newStudent2.id, newStudent2.name, studentGrades))




