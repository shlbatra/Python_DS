def decimaltobinary(num,res=''):
    if num == 0:
        return res

    res= str(num % 2) + res 

    return decimaltobinary(num // 2,res)

input=7
result=''
result=decimaltobinary(input,result)
print(result)