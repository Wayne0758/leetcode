class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        a=0
        for i in range(len(strs)):
            b=0
            if strs[i].isdigit():
                b=int(strs[i])
            else:
                b=len(strs[i])
            if a<b:
                a=b
        return a