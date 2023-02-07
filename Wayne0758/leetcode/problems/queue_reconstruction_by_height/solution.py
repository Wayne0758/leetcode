class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x:x[1])
        people.sort(key = lambda x:-x[0])
        for i in range(1,len(people)):
            cnt=0
            for j in range(i):
                if cnt==people[i][1]:
                    t=people[i]
                    people.pop(i)
                    people.insert(j,t)
                    break
                cnt+=1
        return people