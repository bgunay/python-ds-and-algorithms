# iterative:
def contains(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            return True
    return False

# recursive:


def contains(arr, val, i=0):
    if i >= len(arr):
        return False
    elif arr[i] == val:
        return True
    else:
        return contains(arr, val, i+1)

print(contains([1,2,4,6,7],5))
print(contains([1,2,4,6,7],4))
