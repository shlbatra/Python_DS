class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_map={}
        for i in nums:
            dict_map[i]=dict_map.get(i,0)+1
        print(dict_map)
        for j in nums:
            if dict_map[j] >= 2:
                return True
        return False

    def containsDuplicate_alt(self, nums: List[int]) -> bool:
        hashset=set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
            
        return False