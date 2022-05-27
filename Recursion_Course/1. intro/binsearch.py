def rec(arr, num, left, right):
    mid = (left+right)//2
    if left > right:
        return -1
    elif arr[mid] == num:
        return mid
    elif arr[mid] < num:
        return rec(arr, num, mid+1, right)
    else:
        return rec(arr, num, left, mid-1)


def binarySearch(arr, num):
    left = 0
    right = len(arr)-1
    return rec(arr, num, left, right)


arr = [1, 4, 7, 8, 10, 14, 16, 19, 23, 26, 31, 38, 44, 49]
print(binarySearch(arr, 26))
print(binarySearch(arr, 4))
