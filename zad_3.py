def czy_parzysta(liczba: float) -> bool:
    if liczba % 2 == 0:
        return True
    else:
        return False


x = czy_parzysta(2)

if x:
    print('Liczba jest parzysta')
else:
    print('Liczba jest nieparzysta')
