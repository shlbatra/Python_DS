## Dyanmic Variant

def smallestsum_subarray(arr,k):
    l=0
    running_sum=0
    smallest=float('inf')
    for r in range(0,len(arr)):
        running_sum+=arr[r]
        while running_sum >= k:
            smallest=min(smallest,r-l+1)
            running_sum-=arr[l]
            l=l+1
    return smallest

input=[4,2,2,7,8,1,2,8,10]
targetsum=20
print(smallestsum_subarray(input,targetsum))