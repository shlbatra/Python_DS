#Maximum sum -> Track running sum for maximum
#Size 3 - Window of size 3

#Brute force - Calct all possible subarrays with 2 members 
# and store them in hash table and iterate over hash table 
#Time and Space Complexity -> O(n)


#Sliding Window O(n) & O(1) as keep of left and right index only
def maxsum_subarray(arr,k):
    max_sum = float('-inf')
    run_sum = 0 
    l=0
    for r in range(len(arr)):
            run_sum = run_sum + arr[r]
            if (r-l+1) >= k:
                max_sum=max(max_sum,run_sum)
                run_sum-=arr[l]
                l+=1
    return max_sum
    

input=[4,2,1,7,8,2,8,1,0]
print(maxsum_subarray(input,3))
