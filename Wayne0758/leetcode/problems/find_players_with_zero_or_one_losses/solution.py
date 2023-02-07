class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        d=collections.defaultdict(list)
        a=set()
        for match in matches:
            a.add(match[0])
            a.add(match[1])
            if match[1] not in d:
                d[match[1]]=1
            else:
                d[match[1]]+=1
        b=[]
        c=[]
        for player in a:
            if player not in d:
                b.append(player)
            if d[player]==1:
                c.append(player)
        b.sort()
        c.sort()
        return [b,c]