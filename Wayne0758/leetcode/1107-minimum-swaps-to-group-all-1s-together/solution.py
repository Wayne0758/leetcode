class Solution:
    def minSwaps(self, data: List[int]) -> int:
        num1 = data.count(1)
        res = data[:num1].count(1)
        tmp = res
        i = 0
        while i+num1<len(data):
            if data[i]==1:
                tmp-=1
            if data[i+num1]==1:
                tmp+=1
            res = max(res,tmp)
            i+=1
        return num1-res
