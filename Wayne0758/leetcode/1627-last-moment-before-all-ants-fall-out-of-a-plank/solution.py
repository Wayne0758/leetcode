class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        a, b = 0, 0
        if left:
            a = max(left)
        if right:
            b = n-min(right)
        return max(a, b)
