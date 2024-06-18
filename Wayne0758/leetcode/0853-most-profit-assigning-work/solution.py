class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        worker = sorted(worker)
        difficulty.append(math.inf)
        profit.append(-math.inf)
        zipped = zip(difficulty, profit)
        zipped = sorted(zipped, key = lambda x: x[0])
        index = 0
        res = 0
        maxprofit = 0
        for x, y in zipped:
            while index < len(worker) and worker[index] < x:
                res += maxprofit
                index += 1
            maxprofit = max(y, maxprofit)
        return res
