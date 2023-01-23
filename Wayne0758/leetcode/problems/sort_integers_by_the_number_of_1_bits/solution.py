class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr.sort()
        arr.sort(key = lambda x:bin(x).count("1"))
        return arr