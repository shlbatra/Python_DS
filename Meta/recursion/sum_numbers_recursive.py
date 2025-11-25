# sum_numbers_recursive that takes in an array of numbers and returns the sum of all the numbers in the array
# solve recursively

# sum_numbers_recursive([5, 2, 9, 10]); # -> 26 
# base case return 
# iterate curr number + arr[1:]
# Big O analysis
# Time O(n+1) -> O(n) * array slacing -> O(n/2) -> O(n*n)
# Space O(n) -> fn calls O(n) * array slicing O(n/2) -> O(n*n)


def sum_numbers_recursive(numbers):

    if len(numbers) == 0: # Important base case for smallest where empty array instead of 1 element
        return 0

    return numbers[0] + sum_numbers_recursive(numbers[1:])

arr = [5, 2, 9, 10]
ans = sum_numbers_recursive(arr)
print(ans)

arr = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
ans = sum_numbers_recursive(arr)
print(ans)
