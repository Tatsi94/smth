S = [(-51, 0.1), (2000, 0.2), (584, 0.3), (107, 0.3), (250, 0.1)]

def valid(data):
    res = 0
    for _, j in data:
        res += j

    return abs(res - 1) < 0.0001


def m(data):
    res = 0
    for i, j in data:
        res += i * j

    return res


def d(data):
    res = 0
    ozh = m(data)
    for i, j in data:
        res += j * ((i - ozh) ** 2)

    return res


def main():
    if not valid(S):
        print("Aiaiai")
        return

    print("M = %s" % m(S))
    print("D = %s" % d(S))


main()