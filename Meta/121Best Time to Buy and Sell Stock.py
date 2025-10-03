from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Input [7, 1, 5, 3, 6, 4]
        # Output 5
        # Buy on day 2 and sell on day 5 -> Buy $1 and sell $6
        # Solve as 2 ptr problem
        # left pointer is for buying
        # right pointer is for selling
        # Stay at left ptr and calculate profit by moving right till price is higher
        # If price lower than move left ptr
        # Get max profit
        profit = 0
        l, r = 0, 1
        
        while r < len(prices):
            
            if prices[r] > prices[l]:
                # print(f"{prices[l]}, {prices[r]} and profit {prices[r] - prices[l]}")
                profit = max(prices[r] - prices[l], profit) # get to next lowest pt in profit
            else:
                l = r # start from lowest pt
            r = r + 1 # keep going to next to sell
            # print(i)

        return profit

obj1 = Solution()
ans = obj1.maxProfit([7, 1, 11, 3, 6, 4])
print(ans)