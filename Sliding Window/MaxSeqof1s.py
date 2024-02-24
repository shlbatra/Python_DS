def subarray_maxones(arr,k):
    l=0
    max_len=float('-inf')
    max_arr=[]
    for r in range(len(arr)):
            #Keep moving right and reduce k if see 0
            if arr[r]==0:
                k-=1
            #If we do lose out all k 0s, then move the left ptr 
            #till we get 0 or positive value of k
            while k < 0:
                if arr[l]==0:
                    k+=1
                l+=1
            if len(max_arr) < len(arr[l:r+1]):
                max_arr=arr[l:r+1]
            max_len=max(max_len,r-l+1)
    return max_arr

arr=[0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k=3
print(subarray_maxones(arr,k))


            

