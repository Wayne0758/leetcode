class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums = [-float('inf')] + nums + [float('inf')]
        n = len(nums)
        left, right = 0, n-1
        while left<right:
            mid = (left+right) // 2
            if nums[mid]>=target:
                right = mid
            else:
                left = mid+1
        return right-1
