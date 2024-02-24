class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        val_min = prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            
            val_min =  min(val_min,prices[i])

            max_profit = max(max_profit,prices[i]-val_min)
                
        return max_profit

    def maxProfit_sliding(self, prices: List[int]) -> int:
        '''
        Using sliding algo with 2 pointers left and right
        If left is lower than right, calculate profit and compare
        with max profit also increment r (l is still low)
        If left is higher than right, than right is smaller value 
        and we can point left to right (low value) and increment 
        r to the next value
        '''
        l=0
        r=l+1
        max_profit=0
        while r < len(prices):
            print(f"{prices[l]} & {prices[r]}")
            if prices[l] < prices[r]:
                max_profit = max(max_profit,prices[r]-prices[l])
            else:
                l=r
            r=r+1
        return max_profit


