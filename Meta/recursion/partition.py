# Number of ways you can partition n objects using parts upto m (assuming m>= 0)
# Steps to solve
# 1. What is simplest possible input
# 2. Play around with examples and visualize
# 3. Relate hard cases to simpler cases
# 4. Generalize pattern
# 5. Write code by combining recursive pattern with base case

def count_partitions(n, m):
    if n == 0:
        return 1
    elif m == 1 or n < 0:
        return 0
    # count_partitions(n. m-1) subset of count_partitions(n, m)  + count_partitions(n-m, m)  
    else
        return count_partitions(n, m-1) + count_partitions(n-m, m)