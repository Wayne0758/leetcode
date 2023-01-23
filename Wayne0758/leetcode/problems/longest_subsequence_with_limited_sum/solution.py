class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()
        b=[]
        for i in range(len(queries)):
            a=0
            for j in range(len(nums)):
                if queries[i]>=nums[j] and j!=len(nums)-1:
                    queries[i]-=nums[j]
                    a+=1
                elif queries[i]>=nums[j] and j==len(nums)-1:
                    a+=1
                    b.append(a)
                else:
                    b.append(a)
                    break
        return b