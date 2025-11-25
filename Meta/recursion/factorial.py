#  The factorial of n is the product of all the positive numbers less than or equal to n.
# Base case if 1 then return 1
# iterate current number * (n-1)
# Time O(n) * O(1) = O(n)
# Space O(n) * O(1) = O(n)

def factorial(n):
    if n == 0: return 1 # base case go down to 0 as positive number and return 1, rest get same number to multiply

    return n * factorial(n-1)


ans1 = factorial(6)
print(ans1)
ans2 = factorial(18)
print(ans2)