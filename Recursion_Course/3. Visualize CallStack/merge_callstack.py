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
    print("output: {}".format(output))
    return output


def mergeSort(arr, call_stack):
    call_stack.append('mergeSort('+str(arr)+')')
    print(call_stack)
    if len(arr) < 2:
        call_stack.pop()
        print(call_stack)
        return arr
    else:
        mid = len(arr) // 2
        leftPart = mergeSort(arr[:mid], call_stack)
        rightPart = mergeSort(arr[mid:], call_stack)
        call_stack.pop()
        print(call_stack)
        return joinSorted(leftPart, rightPart)

print(mergeSort([5,3,8,0,12,32,5,7,9,19,11],[]))
print()