class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        res = 0
        cursum = 0
        n = len(arr)
        m = 10**9 + 7
        for i in range(n*min(k,2)):
            cursum = max(cursum + arr[i % n], arr[i % n])
            res = max(res, cursum)
        return max(res, res + sum(arr)*max(0, (k-2))) % m
