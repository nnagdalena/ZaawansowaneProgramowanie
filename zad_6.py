def bosz(a: list, b: list) -> list:
    ab = list(set(a+b))
    for x in range(len(ab)):
        ab[x] = ab[x]**3
    return ab


adin: list = [1, 1, 2, 5]
dva: list = [1, -1, 2, 3]

print(bosz(adin, dva))
