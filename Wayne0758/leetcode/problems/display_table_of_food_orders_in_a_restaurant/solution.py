class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        a=[]
        b=[]
        d=collections.defaultdict(list)
        for order in orders:
            if order[1] not in d:
                d[order[1]]=collections.defaultdict(list)
            if order[2] not in d[order[1]]:
                d[order[1]][order[2]]=1
            else:
                d[order[1]][order[2]]+=1
            if order[2] not in b:
                b.append(order[2])
        b.sort()
        b=['Table']+b
        a.append(b)
        d=sorted(d.items() ,key = lambda x:int(x[0]))
        for k,v in d:
            r=[k]
            for food in b[1:]:
                if food not in v:
                    r.append('0')
                else:
                    r.append(str(v[food]))
            a.append(r)
        return a