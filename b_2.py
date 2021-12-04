lista1: list[float] = [1, 2.1, 3, 4, 5]


def pomnoz(lista: list):
    if len(lista) == 5:
        lista = [x * 2 for x in lista]
        print(lista)


pomnoz(lista1)
