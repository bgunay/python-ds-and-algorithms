# non-tail recursive:
def getMin(arr, i=0):
    if i == len(arr):
        return float('inf')
    else:
        return min(arr[i], getMin(arr, i+1))

# tail-recursive:


def getMin(arr, i=0, acc=float('inf')):
    if i == len(arr):
        return acc
    else:
        return getMin(arr, i+1, min(acc, arr[i]))
