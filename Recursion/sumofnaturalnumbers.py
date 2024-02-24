def sumnaturalnumbers(num,res=0):
    if num <= 1:
        return num   # Sum of 0 is 0 and Sum of 1 is 1 (Base Case)
    return num + sumnaturalnumbers(num-1)

input = 3
res=0
res=sumnaturalnumbers(input,res)
print(res)
