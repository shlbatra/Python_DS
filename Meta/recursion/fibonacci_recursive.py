#  fibonacci, that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.
# The 0-th number of the sequence is 0.
# The 1-st number of the sequence is 1.
# To generate further numbers of the sequence, calculate the sum of previous two numbers.
# base case
# n = 0, 0
# n = 1, 1
# else iterate n-2 + n-1
# Time -> O(2^n) -> each level (n) multiply each parent by 2 children (2^n-1)
# Space -> O(n) -> it returns at the end of base tree for left most branch and then keeps moving right popping and pushing

def fibonacci(n):
    if n<=1: return n

    return fibonacci(n-1) + fibonacci(n-2) 

# Time -> O(n) - each calculated once and once cached, O(1)
# Space -> O(n) -> just taking sum
def fibonacci_efficient(n, memo={}):
    if n<=1: return n

    if n in memo:
        return memo[n] # base case when n already calculated before

    memo[n] = fibonacci_efficient(n-1) + fibonacci_efficient(n-2)  # calculate and store in hash map

    return memo[n] # return for the respective value


# def fibonacci_efficient(n): # Uses memoization




print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(8))
print(fibonacci_efficient(800))