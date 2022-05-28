
#iterative
def getMin(arr):
    minimum = float('inf')
    i = 0
    while i < len(arr):
        minimum = min(arr[i],minimum)

    return minimum


# non-tail recursive:
def getMin(arr, i=0):
    if i == len(arr):
        return float('inf')
    else:
        return min(arr[i], getMin(arr, i+1))


# tail-recursive:
def getMin(arr, i=0, minimum=float('inf')):
    if i == len(arr):
        return minimum
    else:
        print("comparing {} {}".format(minimum, arr[i]))
        return getMin(arr, i+1, min(minimum, arr[i]))


print(getMin([4, 6, 9, 12, 54, 33], 0))
