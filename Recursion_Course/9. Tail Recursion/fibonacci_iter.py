def fib(n):
    prevprev = 0
    prev = 1
    actual = 1
    if n <= 1:
        return n
    else:
        for i in range(2, n):
            prevprev = prev
            prev = actual
            actual = prev+prevprev
        return actual
