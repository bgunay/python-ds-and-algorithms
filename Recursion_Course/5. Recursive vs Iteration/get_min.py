# iterative:
def getMin(arr):
  minVal = float('inf')
  for i in range(len(arr)):
    if arr[i] < minVal:
      minVal = arr[i]
  return minVal
  
# recursive:
def getMin(arr, i=0, minVal=float('inf')):
  if i >= len(arr):
    return minVal
  else:
    if arr[i] < minVal:
      minVal = arr[i]
    return getMin(arr, i+1, minVal)