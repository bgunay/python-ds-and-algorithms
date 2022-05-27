def fib(n, prevprev=0, prev=1, actual=1):
    if n <= 1:
        return n
    elif n == 2:
        return actual
    else:
        prevprev = prev
        prev = actual
        actual = prev+prevprev
        return fib(n-1, prevprev, prev, actual)
