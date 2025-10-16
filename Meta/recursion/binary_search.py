# Use binary search to find a number in array
# assume array is sorted

def binary_search(arr, tgt, left, right):

    if left > right:
        return -1

    mid = int((left+right)/2)
    #print(mid)
    if arr[mid] == tgt:
        return mid

    if arr[mid] < tgt:
        return binary_search(arr, tgt, mid+1, right)
    
    # arr[mid] < tgt
    return binary_search(arr, tgt, left, mid-1)


arr = [-1, 0, 1, 2, 3, 4, 7, 9, 10, 20]

print(binary_search(arr, 10, 0, len(arr)-1))
print(binary_search(arr, 2, 0, len(arr)-1))

print(binary_search(arr, -4, 0, len(arr)-1))
print(binary_search(arr, 8, 0, len(arr)-1))
print(binary_search(arr, 8, 25, len(arr)-1))