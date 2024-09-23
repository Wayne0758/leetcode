class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) == 1:
            return 1
        res = 0
        fruit_type = set([fruits[0],fruits[1]])
        fruit_last = 0
        last_check = 0
        for i in range(1,len(fruits)):
            if fruits[i] not in fruit_type:
                fruit_type = set([fruits[i],fruits[i-1]])
                last_check = fruit_last
            if fruits[i] != fruits[i-1]:
                fruit_last = i
            res = max(res,i-last_check+1)
        return res
