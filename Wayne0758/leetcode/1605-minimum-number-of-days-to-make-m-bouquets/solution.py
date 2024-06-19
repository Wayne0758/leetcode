class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < (m*k):
            return -1
        l = min(bloomDay)
        r = max(bloomDay)
        while l<r:
            mid = (l+r)//2
            if self.getBouquetCount(bloomDay, k, mid) >= m:
                r = mid
            else:
                l = mid+1
        return l
    def getBouquetCount(self, bloomDay: List[int], k: int, waitingDays: int) -> int:
        BouquetCount = 0
        requireFlower = k
        for day in bloomDay:
            if day>waitingDays:
                requireFlower = k
            else:
                requireFlower-=1
                if requireFlower==0:
                    BouquetCount+=1
                    requireFlower = k
        return BouquetCount
