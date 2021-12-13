from klasy.Employee import Employee
from klasy.Student import Student
from klasy.Book import Book
from datetime import date


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
