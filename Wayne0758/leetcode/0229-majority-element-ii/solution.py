class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums)//3
        nums = sorted(nums)
        count = 0
        res = []
        curnum = float('inf')
        for i in range(len(nums)):
            if nums[i]!=curnum:
                if count>threshold:
                    res.append(curnum)
                curnum = nums[i]
                count = 1
            else:
                count += 1
        if count>threshold:
            res.append(nums[-1])
        return res
