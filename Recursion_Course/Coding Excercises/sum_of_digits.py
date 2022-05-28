# Parameters:
#  n: int
# return type: int


def sumOfDigitsMy(n, total=0):
    if n == 0:
        return 0
    digit = (n % 10)
    return digit + sumOfDigitsMy(n//10, total)

# non-tail recursive:


def sumOfDigts(n):
    if n < 0:
        return sumOfDigts(-n)
    elif n < 10:
        return n
    else:
        return (n % 10) + sumOfDigts(n // 10)

# tail recursive:


def sumOfDigits(n, acc=0):
    if n < 0:
        return sumOfDigits(-n)
    elif n < 10:
        return n+acc
    else:
        return sumOfDigits(n//10, acc+n % 10)


print(sumOfDigits(8009))
