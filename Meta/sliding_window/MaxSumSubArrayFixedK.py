# Find max sum subarray of fixed size K
# Ex. [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]

class MaxSumSubArrayK:
    
    def max_sum_subarray_k(self, arr, k):
        max_sum = -9999
        run_sum = 0
        for i in range(0, len(arr)):
            # if i < k:
            #     run_sum += arr[i]
            # else:
            #     run_sum -= arr[i-k]
            #     run_sum += arr[i]
            # max_sum = max(max_sum, run_sum)
            # Alternate efficient approach
            run_sum += arr[i]
            if i >= k-1:
                max_sum = max(max_sum, run_sum)
                run_sum -= arr[i-(k-1)]
        return max_sum
        
arr = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
k = 3

m = MaxSumSubArrayK()
ans = m.max_sum_subarray_k(arr, k)
print(ans)