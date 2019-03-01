vector1 = [2, 6, -7, 9]
vector2 = [7, 80, 32, -1]

mult = zip(vector1,vector2)


def scalar_product(data):
    res = 0
    for i, j in mult:
        res += i * j
    return res

print("Скалярное произведение векторов составляет % s" % scalar_product(mult))