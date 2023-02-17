class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag=0
        for l in s:
            if l=='b':
                flag=1
            if l=='a' and flag==1:
                return False
        return True