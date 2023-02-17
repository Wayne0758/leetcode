class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=[s[0]]
        for i in range(1,len(s)):
            if len(a)!=0 and a[-1]==s[i]:
                a.pop()
            else:
                a.append(s[i])
        return ''.join(a)
