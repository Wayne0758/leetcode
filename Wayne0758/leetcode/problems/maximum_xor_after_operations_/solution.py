from functools import reduce
def orq(x,y):
    return (x | y)
class Solution(object):
    def maximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(orq,nums)