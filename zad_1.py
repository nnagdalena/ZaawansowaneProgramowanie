def powitanie(name: str, surname: str) -> str:
    name_surname = 'Cześć {} {}!'.format(name, surname)
    return name_surname


zmienna = powitanie('Magda', 'Bogacz')

print(zmienna)
