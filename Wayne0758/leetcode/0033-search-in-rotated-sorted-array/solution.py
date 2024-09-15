class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>nums[-1]:
                left = mid+1
            else:
                right = mid-1
        pivot = left
        nums = nums[pivot:]+nums[:pivot]
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return (mid+pivot)%len(nums)
            if nums[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return -1
