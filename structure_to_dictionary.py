
# Convert student information into a dictionary

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


# Create a student object
student = Student("Harshit", 19, "BTech AI & ML")

# Convert object attributes into a dictionary
student_dict = vars(student)

print("Student information as a dictionary:")
print(student_dict)
