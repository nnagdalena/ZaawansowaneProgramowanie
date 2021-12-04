def xyz(x: int, y: int, z: int) -> bool:
    if (x+y) >= z:
        return True
    else:
        return False


print(xyz(1, 1, 3))
