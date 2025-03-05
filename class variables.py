class Student:
    stu_num = 0
    class_year = 2024
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        Student.stu_num += 1
student1 = Student("Oggy", 25)
student2 = Student("Jack", 27)
student3 = Student("Bob", 30)
student4 = Student("Olivia", 24)

print(f"There are {Student.stu_num} students in the {Student.class_year} batch")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)