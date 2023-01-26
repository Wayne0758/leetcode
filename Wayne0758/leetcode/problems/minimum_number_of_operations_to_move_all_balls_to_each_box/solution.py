class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        a=[0 for i in range(len(boxes))]
        for i in range(len(boxes)):
            if boxes[i]=="1":
                for j in range(len(boxes)):
                    a[j]+=abs(i-j)
        return a