__author__ = 'verasraul'




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