class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        a=0
        for i in range(len(piles)//3):
            a+=piles[(-2*(i+1))]
        return a
