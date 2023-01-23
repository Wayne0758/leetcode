class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        a=0
        for j in range(len(strs[0])):
            x=0
            for i in range(len(strs)):
                if x<=ord(strs[i][j]):
                    x=ord(strs[i][j])
                else:
                    a+=1
                    break
        return a