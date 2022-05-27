# non-tail recursive:
def sumToN(n):
    if n == 0:
        return 0
    else:
        return n + sumToN(n-1)

# tail-recursive:


def sumToN(n, acc=0):
    if n == 0:
        return acc
    else:
        return sumToN(n-1, acc+n)
