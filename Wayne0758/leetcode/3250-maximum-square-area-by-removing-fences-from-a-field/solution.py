class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        height=[1]+hFences+[m]
        width=[1]+vFences+[n]
        seth=set()
        setw=set()
        for i in range(len(height)-1,-1,-1):
            for j in range(len(height)):
                seth.add(abs(height[i]-height[j]))
        for i in range(len(width)-1,-1,-1):
            for j in range(len(width)):
                setw.add(abs(width[i]-width[j]))
        samenum = list(seth & setw)
        return (max(samenum)**2)%1000000007 if max(samenum) != 0 else -1
