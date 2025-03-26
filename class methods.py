class Student:
    count = 0
    total_gpa = 0
    # CONSTRUCTOR
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name}: {self.gpa}"
    # CLASS METHOD
    @classmethod
    def total_students(cls):
        return f"Total students are: {cls.count}"
    # CLASS METHOD
    @classmethod
    def avg_gpa(cls):
        return f"Average gpa: {cls.total_gpa/cls.count:.2f}"

student1 = Student(name="Oggy", gpa=3.65)    
student2 = Student(name="Jack", gpa=3.2)    
student3 = Student(name="Bob", gpa=3.4)    
student4 = Student(name="Olivia", gpa=4)    

print(student1.get_info())
print(student2.get_info())
print(student3.get_info())
print(student4.get_info(),"\n")

print(Student.total_students())
print(Student.avg_gpa())