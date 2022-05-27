def joinSorted(arr1, arr2):
  output = []
  i = j = k = 0
  while i < len(arr1) or j < len(arr2):
    if i < len(arr1) and j < len(arr2):
      if arr1[i] < arr2[j]:
        output.append(arr1[i])
        i += 1
      else:
        output.append(arr2[j])
        j += 1
    elif i < len(arr1):
      output.append(arr1[i])
      i += 1
    else:
      output.append(arr2[j])
      j += 1
    k += 1
  return output
  
def mergeSort(arr):
  if len(arr) < 2:
    return arr
  else:
    mid = len(arr) // 2
    leftPart = mergeSort(arr[:mid])
    rightPart = mergeSort(arr[mid:])
    return joinSorted(leftPart, rightPart)