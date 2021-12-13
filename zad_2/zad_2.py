from klasy.Student import Student
from klasy.Library import Library
from klasy.Book import Book
from klasy.Employee import Employee
from klasy.Order import Order
from datetime import date

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
