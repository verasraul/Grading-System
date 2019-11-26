__author__ = 'verasraul'

import uuid

class Student(object):

    def __init__(self, firstname: str, lastname: str):
        self.first = firstname
        self.last = lastname
        self.id = uuid.uuid4()  #Initiate UUID with new Student instance.
        #self.roster = {}
        #self.roster[self.id] = self.name

    def full_name(self):
        return self.first + ' ' + self.last #Combine


    '''def addToRoster(self, id, new_student):
        students =
        self.name = new_student
        self.roster[self.id] = self.name

    def removeFromRoster(self):
        del self.roster[self.id]'''



class Grade(object):

    def __init__(self, grade):
        self.grade = grade
        self.instance_grade = []
        if self.grade is None:
            instancegrade = self.instance_grade
            instancegrade.append(self.grade)


    def get_grades(self):
        #return Grades.grades
        return self.instance_grade



class Roster(object):
    class_roster = []

    def __init__(self, name, id, grades):
        self.name = name
        self.id = id
        self.grades = grades
        self.instance_roster = {}

        instanceroster = self.instance_roster['Student' + Roster.student_count.__str__()] = {}
        instanceroster['name'] = self.name
        instanceroster['id'] = self.id
        instanceroster['grades'] = self.grades

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
student_1_grade = Grade(90)
print('Grade: ', student_1_grade.get_grades())

print('\nAdding 2 more grades to Student 1...')
student_1_grade = Grade(80)
student_1_grade = Grade(70)
print('New Grades: ', student_1_grade.get_grades())


print('\n'+'Printing Student2 grade(s):')
student_2_grade = Grade(60)
print('Grade: ', student_2_grade.get_grades())

print('\nAdding 2 more grades to Student 2...')
student_2_grade = Grade(50)
student_2_grade = Grade(40)
print('New Grades : ', student_2_grade.get_grades())

print('\n'+'Printing Student3 grade(s):')
student_3_grade = Grade(30)
print('Grade: ', student_3_grade.get_grades())

print('\nAdding 2 more grades to Student 3...')
student_3_grade = Grade(20)
student_3_grade = Grade(10)
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