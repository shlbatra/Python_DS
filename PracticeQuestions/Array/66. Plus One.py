# You are given a large integer represented as an integer 
# array digits, where each digits[i] is the ith digit of 
# the integer. The digits are ordered from most significant 
# to least significant in left-to-right order. The large 
# integer does not contain any leading 0's.

# Increment the large integer by one and return the 
# resulting array of digits.


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # for i in range(len(digits)-1,0,-1):
        #    if i == len(digits)-1:
        
        n = len(digits)
        
        for i in range(n-1,-1,-1):
            digits[i] = digits[i] + 1
            if digits[i] < 10:
                return digits
            else: #00
                digits[i] = 0
                
        digits.insert(0,1)
        return digits