class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        mx = 0
        conversion = 0
        res = [0]
        for num in nums:
            if num>mx:
                mx = num
            conversion = mx+num
            res.append(res[-1]+conversion)
        return res[1:]
