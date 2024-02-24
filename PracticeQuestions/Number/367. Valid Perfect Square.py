class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = ceil(num/2)
        while start <= end:
            mid = int((start+end)/2)
            print(mid)
            mid_square = mid*mid 
            if mid_square < num:
                start = mid+1
            elif mid_square > num:
                end = mid-1
            elif mid_square == num:
                return True
        return False