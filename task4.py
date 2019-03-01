n = 10
m = 2
s = 6

k = n - m


def factorial(data):
    if data == 0:
        return 1
    else:
        return data * factorial(data - 1)

def probability(data):
    res = (factorial(n) / (factorial(m) * factorial(k))) * (((7 - s) / 6)**m) * (1 - ((7 - s) / 6))**k
    return res

print("Вероятность составляет % s" % probability(factorial))