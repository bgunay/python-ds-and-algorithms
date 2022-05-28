# iteration
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


# recursive
def fibRec(n):
    if n < 1:
        return n
    else:
        return fibRec(n-1) + fibRec(n+1)

# tail rec
def fibTailRec(n, prevprev=0, prev=1, actual=1):
    if n <= 1:
        return n
    elif n == 2:
        return actual
    else:
        prevprev = prev
        prev = actual
        actual = prev + prevprev
        return fibTailRec(n-1, prevprev, prev, actual)


print(fibTailRec(8))
