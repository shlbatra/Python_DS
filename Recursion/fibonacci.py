def fibonacci(num):
    if num == 0 or num == 1:
        return num 
    return fibonacci(num-1) + fibonacci(num-2)

def fibonacci_map(num):
    dict_ans={}
    dict_ans[0]=0
    dict_ans[1]=1
    def fibonacci(num):
        if num in dict_ans:
            return dict_ans[num]
        ans=fibonacci(num-1) + fibonacci(num-2) 
        dict_ans[num]=ans
        return ans
    return fibonacci(num)


print(fibonacci(6))
print(fibonacci_map(6))