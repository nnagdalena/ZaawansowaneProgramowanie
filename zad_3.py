class Property:
    area: str
    rooms: int
    price: float
    address: str

    def __init__(self, area: str, rooms: int, price: float, address: str) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f'The property has following attributes: area - {self.area}; {self.rooms} rooms; price (in PLN) - {self.price}; address: {self.address}. '


class House(Property):
    plot: int

    def __init__(self, area: str, rooms: int, price: float, address: str, plot: int):
        Property.__init__(self, area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f'This house has following attributes: area - {self.area}; {self.rooms} rooms; price (in PLN) - {self.price}; address: {self.address}; plot - {self.plot}. '


class Flat(Property):
    floor: int

    def __init__(self, area: str, rooms: int, price: float, address: str, floor: int):
        Property.__init__(self, area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f'This flat has following attributes: area - {self.area}; {self.rooms} rooms; price (in PLN) - {self.price}; address: {self.address}; floor - {self.floor}. '


# p = Property('Centrum', 3, 123456.98, 'Mickiewicza 20')
# print(p)

h = House('Koszutka', 6, 99999999.99, 'Iłłakowiczówny 20', 5555)
print(h)

f = Flat('Brynów', 2, 12345, 'Gawronów 20', 12345)
print(f)
