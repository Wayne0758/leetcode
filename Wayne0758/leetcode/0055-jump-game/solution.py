class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        can_reach = [0] * n
        can_reach[-1] = 1
        tmp = n-1
        
        for i in range(n-2,-1,-1):
            if i+nums[i]>=tmp:
                tmp = min(tmp,i)
        if tmp==0:
            return True
        return False
