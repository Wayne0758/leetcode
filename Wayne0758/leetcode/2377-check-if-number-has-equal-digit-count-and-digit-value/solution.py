class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        flag=True
        for i in range(len(num)):
            a=num.count(str(i))
            if int(num[i])!=a:
                flag=False
        return flag
