class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(len(prices)):
            flag=0
            for j in range(i+1,len(prices)):
                if prices[j]<=prices[i]:
                    a.append(prices[i]-prices[j])
                    flag=1
                    break
            if flag==0:
                a.append(prices[i])
        return a
