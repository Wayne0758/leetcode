class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        sumnums=sum(nums)
        for num in nums:
            if (sumnums-num)<=num:
                sumnums-=num
            else:
                return sumnums
        return -1
