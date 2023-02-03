from collections import defaultdict, Counter
class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        d=defaultdict(set)
        for id, time in logs:
            d[id].add(time)
        c=Counter(len(times) for times in d.values())
        return [c[i] for i in range(1,k+1)]
        