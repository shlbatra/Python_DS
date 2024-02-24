#Write an algorithm to determine if a number n is happy.

#A happy number is a number defined by the following process:

#Starting with any positive integer, replace the number by the sum of the squares of its digits.
#Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#Those numbers for which this process ends in 1 are happy.

class Solution:
    def isHappy(self, n: int) -> bool:
        result = 0
        seen = set()
        
        while n not in seen:
            result=0
            seen.add(n)
            while n>0:
                result = result + (n%10)**2
                n = int(n/10)
            n = result
            print(n)
            if n == 1:
                return True
        return False