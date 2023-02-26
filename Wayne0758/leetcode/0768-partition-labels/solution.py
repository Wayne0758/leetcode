class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        res=[0]
        end=collections.defaultdict(int)
        for i in range(len(s)):
            end[s[i]]=i
        a=0
        for i in range(len(s)):
            a=max(a,end[s[i]])
            if a==i:
                res.append(a-sum(res)+1)
        return res[1:]
