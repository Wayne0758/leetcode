class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        a=nums1+nums2+nums3
        c=[]
        for i in range(len(a)):
            b=0
            if a[i] in nums1:
                b+=1
            if a[i] in nums2:
                b+=1
            if a[i] in nums3:
                b+=1
            if b>=2 and a[i] not in c:
                c.append(a[i])
        return c