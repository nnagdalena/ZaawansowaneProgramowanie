class Student:
    name: str
    marks: int

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if self.marks > 50:
            return True
        else:
            return False


student1 = Student("Madzia", 100)
student2 = Student("Wiktoria z Hotelu Paradise", 20)

print(student1.is_passed())
print(student2.is_passed())
