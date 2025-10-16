# Non optimized as recursion for left finishes first and then right
# Do same thing again and again -> so code can be optimized; do redundant calculations for ex. f(3) -> optimization to avoid recalculating for what we have done before
# Optimization technique called memoization

# FO=1; F1=1
# FN = FN-1 + FN-2

def fibonacci(n):
    if n == 0 or n==1: return n
    else:
        return fibonacci(n-1)+fibonacci(n-2) # recursion for left finishes first and then right

print(fibonacci(6))