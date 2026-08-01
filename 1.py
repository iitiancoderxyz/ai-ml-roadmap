import json
class StudentTracker:
    def __init__(self):
        self.students={}
    def add_grade(self, student_name, subject, score):
        if student_name not in self.students:
            self.students[student_name]={}
        self.students[student_name][subject]=score 
    def get_student_average(self, student_name):
        if student_name not in self.students:
            return None 
        grades=self.students[student_name]
        if len(grades)==0:
            return 0 
        return sum(grades.values())/len(grades)
    def save_data(self):
        with open("grades.json","w") as f:
            json.dump(self.students,f,indent=4)

        


    