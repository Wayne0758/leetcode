class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        n=len(height)
        mx_height = 0
        left = []
        for i in range(n):
            mx_height = max(mx_height,height[i])
            left.append(mx_height)
        mx_height = 0
        right = []
        for i in range(n-1,-1,-1):
            mx_height = max(mx_height,height[i])
            right.append(mx_height)
        right = sorted(right,reverse = True)
        for i in range(n):
            res+= min(left[i],right[i])-height[i]
        return res
