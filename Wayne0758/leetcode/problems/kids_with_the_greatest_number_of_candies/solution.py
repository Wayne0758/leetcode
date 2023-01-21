class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        a=0
        b=[]
        for i in range(len(candies)):
            a=candies[i]+extraCandies
            candies.append(a)
            b.append(a==max(candies))
            candies.pop()
        return b

