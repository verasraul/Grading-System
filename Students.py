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
        instanceroster['NAME'] = self.name
        instanceroster['ID'] = self.id
        instanceroster['GRADES'] = self.grades

        Roster.class_roster.append(self.instance_roster)

    def get_student_info(self):
        return (self.instance_roster)



print('Creating 3 new Student instances from Student class'.upper())
print('...')
print('creating Student1...')
student_1 = Student('Jane', 'Doe')
print('--complete--'.upper())

print('\ncreating Student2...')
student_2 = Student('John', 'Doe')
print('--complete--'.upper())

print('\ncreating Student3...')
student_3 = Student('Jim', 'Doe')
print('--complete--'.upper())


print('\nprinting new student instance name and ID:'.upper())
print('\n',student_1.full_name(), student_1.id)
print('\n',student_2.full_name(), student_2.id)
print('\n',student_3.full_name(), student_3.id)


print('\n'+'Printing Student1 grade(s):')
student_1_grade = Grades(90)
print('Grade: ', student_1_grade.get_grades())

print('\nAdding 2 more grades to Student 1...')
student_1_grade.add_grade(80)
student_1_grade.add_grade(70)
print('New Grades: ', student_1_grade.get_grades())


print('\n'+'Printing Student2 grade(s):')
student_2_grade = Grades(60)
print('Grade: ', student_2_grade.get_grades())

print('\nAdding 2 more grades to Student 2...')
student_2_grade.add_grade(50)
student_2_grade.add_grade(40)
print('New Grades : ', student_2_grade.get_grades())

print('\n'+'Printing Student3 grade(s):')
student_3_grade = Grades(30)
print('Grade: ', student_3_grade.get_grades())

print('\nAdding 2 more grades to Student 3...')
student_3_grade.add_grade(20)
student_3_grade.add_grade(10)
print('New Grades : ', student_3_grade.get_grades())

print('\n'+'Converting results to dictionary:'.upper())
print('...')
print('...')
print('...')
roster_instance_1 = Roster(student_1.full_name(), student_1.id, student_1_grade.get_grades())
roster_instance_2 = Roster(student_2.full_name(), student_2.id, student_2_grade.get_grades())
roster_instance_3 = Roster(student_3.full_name(), student_3.id, student_3_grade.get_grades())

print('\n'+'Viewing instance info with \'get_student_info\' method:'.upper())
print(roster_instance_1.get_student_info())
print(roster_instance_2.get_student_info())
print(roster_instance_3.get_student_info())

print('\n'+'Viewing class info by calling \'Roster.class_roster\' attribute'.upper())
print(Roster.class_roster)