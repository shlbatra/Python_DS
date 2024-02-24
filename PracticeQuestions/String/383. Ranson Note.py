#Given two stings ransomNote and magazine, return true 
# if ransomNote can be constructed from magazine and 
# false otherwise.

#Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct_best(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = collections.Counter(magazine)
        for i in ransomNote:
            if magazine_map.get(i,0) == 0:
                return False
            magazine_map[i] -=1
        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = collections.Counter(magazine)
        ransomNote_map = collections.Counter(ransomNote)
        for i in ransomNote_map:
            if (magazine_map.get(i,0) - ransomNote_map.get(i,0)) < 0:
                return False
        return True