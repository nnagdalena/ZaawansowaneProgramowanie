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
