# Find number in sorted list of numbers and tgt
# O(logn)

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = int((left+right)/2)
        #print(left, right, mid)
        if numbers[mid] == target:
            return mid
        elif numbers[mid] > target: # [0,0,0, 2, 3, 4] 0
            right = mid - 1
        else:
            left = mid + 1

    return -1

ans1 = binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8], 6)
print(ans1)