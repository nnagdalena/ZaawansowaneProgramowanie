from klasy.Library import Library
from datetime import date


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
