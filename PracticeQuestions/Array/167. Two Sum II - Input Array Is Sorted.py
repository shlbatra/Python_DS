class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sliding window solution
        l,r=0,len(numbers)-1

        while l < r:
            if (numbers[l]+numbers[r])<target:
                l=l+1
            elif (numbers[l]+numbers[r])>target:
                r=r-1
            else:
                return([l+1,r+1])

    def twoSum_bruteforce(self, numbers: List[int], target: int) -> List[int]:
        print(len(numbers))
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if(numbers[i]+numbers[j])==target:
                    return([i+1,j+1])
                if(numbers[i]+numbers[j])>target:
                    break