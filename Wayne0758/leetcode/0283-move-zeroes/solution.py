class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        non_zeros = []
        for num in nums:
            if num == 0:
                zeros.append(0)
            else:
                non_zeros.append(num)
        i = 0
        while i<len(nums):
            if non_zeros:
                nums[i] = non_zeros.pop(0)
            else:
                nums[i] = zeros.pop(0)
            i+=1
