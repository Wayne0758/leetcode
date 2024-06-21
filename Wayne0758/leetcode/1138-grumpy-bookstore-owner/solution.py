class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        a = 0
        for i in range(len(grumpy)):
            if grumpy[i] == 0:
                a += customers[i]
        maxvalue = a
        for i in range(len(customers)-minutes+1):
            tmp = a
            for j in range(i,i+minutes):
                if grumpy[j] == 1:
                    tmp += customers[j]
            maxvalue = max(maxvalue,tmp)
        return maxvalue
