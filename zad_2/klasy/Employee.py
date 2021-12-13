from datetime import date


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
