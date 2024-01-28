
def myPow(x, n):
    res = 1
    for i in range(n):
        res *= x
    return res


print(myPow(2,3))