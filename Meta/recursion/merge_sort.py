# Use merge sort for array
# split array in half -> start with left side first
# continue divide to left till get individual elememt
# base case -> compare single values and merge and sort
# then continue on right side 
# Final merge - linear comparison with 2 ptrs -> whichever is small get first and then remaining place at end.


def merge_sort(arr):
    if len(arr) <= 1: # base case array already sorted
        return arr

    # divide array in halves
    mid = int(len(arr)/2)
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    res = merge(left, right) # linear time comparison to put values in correct order
    return res

def merge(left, right):
    # build temp array to avoid modifying original content
    tmp = []
    i, j = 0, 0

    # while both sub arrays have values, then merge in sorted order
    while i<len(left) and j < len(right): 
        if left[i] <= right[j]:
            tmp.append(left[i])
            i+=1
        else:
            tmp.append(right[j])
            j+=1
    # Left over left or right sub arrays to result
    while (i<len(left)):
        tmp.append(left[i])
        i+=1
    while (j<len(right)):
        tmp.append(right[j])
        j+=1
    return tmp

arr = [8,2,4,90,12,-9,-8,0,1,-98]
print(merge_sort(arr))

