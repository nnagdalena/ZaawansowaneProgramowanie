lista1: list[str] = ['Jarek', 'Darek', 'Marek', 'Szuwarek', 'Joachim']


def print_list(lista: list):
    if len(lista) == 5:
        for x in range(len(lista)):
            print(lista[x])


print_list(lista1)
