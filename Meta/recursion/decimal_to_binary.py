# Convert decimal base 10 to binary 2 
# 233 // 2  -> 1
# 116 // 2  -> 0
# 58 // 2 -> 0
# 29 // 2 -> 1
# 14 // 2 -> 0
# 7 // 2 -> 1
# 3 // 2 -> 1
# 1 // 2 -> 1

# Get same order as pushed onto stack 

def decimal_to_binary(num):
    # Base case
    if num <= 1: return str(num)
    # recursive code
    return decimal_to_binary(int(num/2)) + str(num%2) 
          # move to next step + minor solution as stack need last item to be returned first

def decimal_to_binary_alternate(num, res):
    if num == 0: return res
    res = str(num % 2) + res
    return decimal_to_binary_alternate(int(num/2), res)

print(decimal_to_binary(233)) 
print(decimal_to_binary_alternate(233,"")) 