class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:

        stones_dict={}
        stones_dict=collections.Counter(stones)
        result=0
        for i in jewels:
            result = result + stones_dict.get(i,0)
        return result

    def numJewelsInStones_set(self, jewels: str, stones: str) -> int:
        
        check_j = set(jewels)
        result=0
        for i in stones:
            if i in check_j:
                result+=1
        return result