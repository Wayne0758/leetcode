class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(len(nums1)):
            flag1=0
            flag2=0
            b=0
            for j in range(len(nums2)):
                if nums1[i]==nums2[j] and j!=len(nums2)-1:
                    flag2=1
                if flag2==1 and nums2[j]>nums1[i]:
                    a.append(nums2[j])
                    break
                if j==len(nums2)-1:
                    a.append(-1)
                    break
        return a