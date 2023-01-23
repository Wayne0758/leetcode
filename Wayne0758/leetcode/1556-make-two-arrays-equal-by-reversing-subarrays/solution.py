class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        for i in range(len(target)):
            if target[i] in arr:
                arr.remove(target[i])
            else:
                return False
        return True
