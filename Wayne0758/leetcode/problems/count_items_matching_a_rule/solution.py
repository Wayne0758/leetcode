class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        a=["type","color","name"]
        b=0
        for i in range(3):
            if ruleKey==a[i]:
                b=i
        c=0
        for i in range(len(items)):
            if items[i][b]==ruleValue:
                c+=1
        return c