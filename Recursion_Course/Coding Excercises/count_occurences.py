# Parameters:
#  arr: List[int]
#  num: int
# return type: int

def countOccurrencesMy(arr, num, i, total):
    if i == len(arr):
        return total
    if arr[i] == num:
        return countOccurrencesMy(arr, num, i+1, total+1)
    else:
        return countOccurrencesMy(arr, num, i+1, total)

# non-tail recursive:


def countOccurrences(arr, num, i=0):
    if i == len(arr):
        return 0
    elif arr[i] == num:
        return 1 + countOccurrences(arr, num, i+1)
    else:
        return countOccurrences(arr, num, i+1)

# tail recursive:
def countOccurrencesTail(arr, num, i=0, acc=0):
    if i == len(arr):
        return acc
    elif arr[i] == num:
        return countOccurrencesTail(arr, num, i+1, acc+1)
    else:
        return countOccurrencesTail(arr, num, i+1, acc)


arr = [4, 2, 7, 4, 4, 1, 2]
num = 4
print(countOccurrencesMy(arr, num, 0, 0))
