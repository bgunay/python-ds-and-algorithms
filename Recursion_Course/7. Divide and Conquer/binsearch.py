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
