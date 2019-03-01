vector = [2, 5, 8]

def vector_length(data):
    res = 0
    res += (sum(i**2 for i in vector)**0.5)
    return res


print("Длина вектора составляет % s" % vector_length(vector))