def fact(n, acc=1):
    if n == 1:
        return acc
    else:
        return fact(n-1, acc*n)
