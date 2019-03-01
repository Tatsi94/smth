n = 10
m = 2
s = 6

k = (n - m)

def fact(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fact(m):
    result = 1
    for i in range(2, m + 1):
        result *= i
    return result

def fact(k):
    result = 1
    for i in range(2, k + 1):
        result *= i
    return result


def probability(data):
    res = (fact(n) / (fact(m) * fact(k))) * (((7 - s) / 6)**m) * (1 - ((7 - s) / 6))**k
    return res

print("Вероятность составляет % s" % probability(fact))