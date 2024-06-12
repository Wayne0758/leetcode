class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=[0,0,0]
        for num in nums:
            a[num]+=1
        count=0
        for i in range(len(a)):
            for j in range(a[i]):
                nums[count] = i
                count+=1
