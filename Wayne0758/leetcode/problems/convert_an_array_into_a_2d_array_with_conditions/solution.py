class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        a=[[]]
        for i in nums:
            for j in range(len(a)):
                if i not in a[j]:
                    a[j].append(i)
                    break
                else:
                    if j==len(a)-1:
                        a.append([i])
                        break
        return a