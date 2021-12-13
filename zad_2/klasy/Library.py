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
