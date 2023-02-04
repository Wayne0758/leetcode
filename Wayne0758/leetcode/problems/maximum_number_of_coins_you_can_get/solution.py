class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        s=0
        piles.sort()
        n=len(piles)/3
        piles=piles[n:]
        for i in range(n):
            piles.pop()
            a=piles.pop()
            s+=a
        return s