class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        a=0
        for i in range(len(accounts)):
            b=sum(accounts[i])
            if b>a:
                a=b
        return a