# non-tail recursive:
def pow(a, b):
    if b == 0:
        return 1
    else:
        return a*pow(a, b-1)

# tail-recursive:


def pow(a, b, acc=1):
    print("{} {} {}".format(a,b,acc))
    if b == 0:
        return acc
    else:
        return pow(a, b-1, acc*a)

print(pow(33,2,1))

