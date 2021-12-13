class Student:
    name: str
    marks: int

    def __init__(self, name, marks) -> None:
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if self.marks > 50:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f'Imię: {self.name} - {self.marks}/100%'
