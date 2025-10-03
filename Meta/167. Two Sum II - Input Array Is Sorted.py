from typing import List

class Solution:
    # How to add 2 number combinations and get to target
    # [2, 7, 11, 15] target 9 
    # indexes are not 0 based
    # each input has one solution only
    # Not use same element twice
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sliding window solution
        # sorted list assumption
        # -1 + 2 -> 1 -> greater than target reduce right
        # -1 + 1 => 0
        l,r=0,len(numbers)-1

        while l < r:
            if (numbers[l]+numbers[r])<target:
                l=l+1
            elif (numbers[l]+numbers[r])>target:
                r=r-1
            else:
                return([l+1,r+1]) # arrays are 0 indexed

    def twoSum_bruteforce(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if(numbers[i]+numbers[j])==target:
                    return([i+1,j+1])
                if(numbers[i]+numbers[j])>target:
                    break

    def twoSum_hashmap(self, numbers: List[int], target: int) -> List[int]:
    # Investigate 2 sum approach with HashMap later on
    #     # investigate how this will work for duplicate entries
        h_map = {}
    #     # [2, 7, 11, 15] target 9 
    #     # 2: 0
    #     # 2:0, 7: 1
    #     # 
        for i in range(len(numbers)):
            if (target - numbers[i]) in h_map:
                return [i+1, h_map[target - numbers[i]]+1]
            h_map[numbers[i]] = i
            
obj1 = Solution()
ans = obj1.twoSum_hashmap([2, 7, 11, 15], 13)
print(ans)
