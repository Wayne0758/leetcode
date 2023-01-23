class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        a=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                a.append(nums1[i])
        b=[]
        for i in range(len(nums1)):
            if nums1[i] not in a and nums1[i] not in b:
                b.append(nums1[i])
        c=[]
        for i in range(len(nums2)):
            if nums2[i] not in a and nums2[i] not in c:
                c.append(nums2[i])
        return [b,c]
