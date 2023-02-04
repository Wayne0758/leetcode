class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        a=capacity
        s=0
        for i in range(len(plants)):
            if a>=plants[i]:
                a-=plants[i]
                s+=1
            else:
                a=capacity-plants[i]
                s+=2*i+1
        return s