n = 10
m = 2
s = 6

k = n - m


def factorial(data):
    res = 1
    for data in range(1, data-1):
        res = data * (factorial(data - 1))
    return res


def probability(data):
    res = (factorial(n) / (factorial(m) * factorial(k))) * (((7 - s) / 6)**m) * (1 - ((7 - s) / 6))**k
    return res


print("Вероятность составляет % s" % probability(factorial))