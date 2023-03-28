student ={"name":"Rolf", "grades":(89, 90,93,90)}

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grades(self):
        return sum(self.grades)/len(self.grades)
        

student = Student("Bob", (92,90,93,98,90))
student2 = Student("Rolf", (92,59,93,89,88))

print(student.average_grades())
print(student2.average_grades())