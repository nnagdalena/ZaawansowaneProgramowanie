lista1: list[float] = [1, 2, 3, 4.1, 5]


def pomnoz(lista: list):
    if len(lista) == 5:
        for x in range(len(lista)):
            lista[x] = lista[x] * 2
        print(lista)


pomnoz(lista1)
