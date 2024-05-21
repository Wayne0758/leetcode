class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        xornums=[]
        res=sum(nums)
        for num in nums:
            xornums += [[num, num ^ k]]
        xornums = sorted(xornums, key = lambda xornum: -(xornum[1]-xornum[0]))
        while len(xornums)>1:
            if xornums[0][1]-xornums[0][0] + xornums[1][1]-xornums[1][0] >0:
                res += xornums[0][1]-xornums[0][0] + xornums[1][1]-xornums[1][0]
                xornums.pop(0)
                xornums.pop(0)
            else:
                break
        return res
