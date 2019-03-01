n = 3
m = 5

def check(n):
    number = 0
    if len(str(n)) == len(str(m)):
        number += round((((10**n)-1) - 10**(n-1)) / m)
        return number
    else:
        print("zero")


print("Количество %s" % n, "-значных чисел, делящихся на %s" % m,", составляет % s" % check(n))