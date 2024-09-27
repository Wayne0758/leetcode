class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = 10001
        mx = 0
        for price in prices:
            if price<mn:
                mn = price
            elif price - mn > mx:
                mx = price - mn
        return mx
