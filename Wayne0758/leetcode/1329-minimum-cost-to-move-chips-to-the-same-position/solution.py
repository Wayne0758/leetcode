class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        for i in range(len(position)):
            position[i]=position[i]%2
        a=position.count(0)
        b=position.count(1)
        return min(a,b)
