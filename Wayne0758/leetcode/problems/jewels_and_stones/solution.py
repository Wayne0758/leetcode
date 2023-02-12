class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        a=0
        for stone in stones:
            if stone in jewels:
                a+=1
        return a