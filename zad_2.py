from datetime import date


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


class Library:
    city: str
    street: str
    zip_code: str
    open_hours: str
    phone: str

    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str) -> None:
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f'Miasto: {self.city}, \nAdres: {self.street}, \nKod pocztowy {self.zip_code}, \nGodziny otwarcia: {self.open_hours}, \nNr tel: {self.phone}'


class Employee:
    first_name: str
    last_name: str
    hire_date: date
    city: str
    street: str
    zip_code: str
    phone: str

    def __init__(self, first_name: str, last_name: str, hire_date: date, city: str, street: str,
                 zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Imię: {self.first_name}, \nNazwisko: {self.last_name}, ' \
               f'\nData zatrudnienia: {self.hire_date}, \nMiasto: {self.city}, \nUlica: {self.street}, \nKod pocztowy: {self.zip_code}, \nNr telefonu: {self.phone}'


class Book:
    library: Library
    public_date: date
    author_name: str
    author_surname: str
    number_of_pages: int

    def __init__(self, library: Library, publication_date: date, author_name: str, author_surname: str,
                 number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Data publikacji {self.publication_date},\nImię autora: {self.author_name}, ' \
               f'\nNazwisko autora: {self.author_surname}, \nLiczba stron: {self.number_of_pages}, \nBiblioteka: {self.library}'


class Order:
    employee: Employee
    student: Student
    books: Book
    order_date: date

    def __init__(self, employee: Employee, student: Student, books: Book, order_date: date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'Data zamówienia {self.order_date}, \nPracownik: \n{self.employee}, \nStudent: \n{self.student}, \nKsiążka: \n{self.books}. \n'


l1 = Library('Katowice', 'Mickiewicza 20', '40-099', '8-16', '555666777')
l2 = Library('Katowice', 'Słowackiego 22', '40-095', '7-18', '11223344')

b1 = Book(l1, date(2021, 11, 1), 'Philip', 'K. Dick', 1000)
b2 = Book(l1, date(2021, 11, 2), 'Philip', 'K. Dick', 200)
b3 = Book(l1, date(2021, 11, 3), 'Philip', 'K. Dick', 300)
b4 = Book(l2, date(2021, 11, 4), 'Philip', 'K. Dick', 400)
b5 = Book(l2, date(2021, 11, 5), 'Philip', 'K. Dick', 500)

e1 = Employee('Madzia', 'Bogacz', date(2020, 1, 1), 'Sosnowiec', 'ul. Kochanowskiego', '40-098', '12345678')
e2 = Employee('Madzia', 'Kulczyk', date(2021, 1, 1), 'Bytom', 'ul. Matejki', '40-099', '111111111')
e3 = Employee('Madzia', 'Bezos', date(2019, 1, 1), 'Będzin', 'ul. Przemka z Hotelu Paradise',
              '40-097', '222222')

s1 = Student('Jadwiga', 90)
s2 = Student('Janina', 99)

o1 = Order(e1, s1, b1, date(2021, 11, 23))
o2 = Order(e3, s2, b5, date(2021, 11, 22))

print(o1)
print(o2)
