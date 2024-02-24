
def subarray_target(arr,target):
    l=0 
    res=[]
    run_sum=0
    for r in range(len(arr)):
        run_sum=run_sum+arr[r]
        while run_sum >= target:
            if run_sum == target:
                res.append(arr[l:r+1])
            run_sum -= arr[l]
            l=l+1
    return res

#Works 
inputarray = [23, 1, 6, 9, 15, 8]
target=24
print(subarray_target(inputarray,target))

#Solution doesnt work correctly
inputarray = [-1, -4, 0,5, 3, 2, 1]
target=5
print(subarray_target(inputarray,target))
#With negative values, sliding window shrinks even when expanding
#Solve by finding lowest possible number and increment it by 
# positive number such that all numbers possible (lowest possible+1)








