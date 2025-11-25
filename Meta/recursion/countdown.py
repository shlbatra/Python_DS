def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)
    # print(n) -> if here get in reverse order 
    # countdown(n-2) # infinite loop for odd as base case not catches it and for even, just get even numbers

countdown(10)
print("\n")
countdown(9)