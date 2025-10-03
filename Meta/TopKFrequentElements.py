from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Input: nums = [1,2,2,3,3,3], k = 2
        # Output: [2,3]
        # Input: nums = [7,7], k = 1
        # Output: [7]
        
        # Slightly worse algo
        # use hashmap to track freq for each
        # return top k sorted based on values
        # 1 - 1, 2 - 2, 3 - 3
        print(k)
        h_map = {}

        for n in nums:
            h_map[n] = h_map.get(n, 0) + 1

        arr = []
        for num, cnt in h_map.items():
            arr.append([cnt, num])
        arr.sort()
#        print(arr)
        res = []
        while len(res) < k:
#           print(len(res))
#           print(k)
            res.append(arr.pop()[1])

        return res

    # Bucket sort algo
    def topKFrequent_bucketsort(self, nums: List[int], k: int) -> List[int]:

        # Input: nums = [1,2,2,3,3,3], k = 2
        # Output: [2,3]

        # 0, 1, 2, 3, 4, 5, 6
        # , [1], [2], [3], , 
        h_map = {}
        freq = [[] for i in range(len(nums) + 1)] # code for initializing bucket
        for n in nums:
            h_map[n] = h_map.get(n, 0) + 1

        for num, cnt in h_map.items():
            freq[cnt].append(num)

        
        res=[]
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:  # for each bucket, add num till get top k
                res.append(num)
                if len(res) == k:
                    return res



# obj1 = Solution()
# ans1 = obj1.topKFrequent_bucketsort(nums = [1,2,2,3,3,3], k = 2)
# print(ans1)

obj2 = Solution()
ans2 = obj2.topKFrequent_bucketsort(nums = [2,2], k = 1)
print(ans2)