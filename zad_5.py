def funkcja(lista: list, liczba: int) -> bool:
    if liczba in lista:
        return True
    else:
        return False


a: list = [1, 2, 3, 5, 4]
b = 45

print(funkcja(a, b))
