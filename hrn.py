vector1 = [2, 6, -7, 9]
vector2 = [7, 80, 32, -1]

mult = zip(vector1,vector2)
print(list(mult))
for i, j in mult:

    vector1 = [2, 6, -7, 9]
    vector2 = [7, 80, 32, -1]

    mult = zip(vector1, vector2)

    res = 0

    for i, j in mult():
        res += i * j

    return res