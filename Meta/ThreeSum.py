from typing import List

class Solution:
    # How to add 2 number combinations and get to target
    # [-1, 0, 1, 2] target 0 
    def threeSum(self, numbers: List[int], target: int) -> List[list]:
        res = []
        numbers.sort() # sorting important to skip same values
        # -3 -3 1 2 3 4; target 0
        print(numbers)
        # Need two loops for main and then l-r approach
        # Smart way to append i or l if same values only after incrementing first time
        for i in range(len(numbers)):
            if numbers[i] == numbers[i-1] and i > 0:
                continue
            l, r = i+1, len(numbers)-1
            tgt = target - numbers[i]
            # print(f"{l}-{r}")
            # print(f"{numbers[i]}-{numbers[l]}-{numbers[r]}")
            while l < r:
                if numbers[l] + numbers[r] < tgt:
                    l = l+1
                if numbers[l] + numbers[r] > tgt:
                    r = r-1
                if numbers[l] + numbers[r] == tgt:
                    res.append([numbers[i],numbers[l],numbers[r]])
                    l=l+1
                while numbers[l] == numbers[l-1] and l < r:
                    l=l+1
            return res

obj1 = Solution()
ans = obj1.threeSum([3, -3, 1, 2, -3, 4], 0)
print(ans)