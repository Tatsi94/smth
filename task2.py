vector1 = [2, 6, -7, 9]
vector2 = [7, 80, 32, -1]


def scalar_product(a, b):
    multiplication = zip(vector1, vector2)
    res = 0
    for i, j in multiplication:
        res += i * j
    return res


print("Скалярное произведение векторов составляет % s" % scalar_product(vector1, vector2))