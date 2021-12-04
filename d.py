lista1: list[float] = [1, 2, 3, 4, 5, 55, 44, 33, 22, 11]


def pokaz_co_drugi(lista: list):
    if len(lista) == 10:
        for x in range(10):
            if x % 2 == 0:
                print(lista[x])


pokaz_co_drugi(lista1)
