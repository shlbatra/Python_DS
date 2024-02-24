class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            b=(n>>i)%2
            res=res | (b<<(31-i))
        return res