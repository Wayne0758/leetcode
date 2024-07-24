class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        Jumbled_value = []
        for num in nums:
            str_num = str(num)
            s = ''
            for c in str_num:
                s += str(mapping[int(c)])
            Jumbled_value.append(int(s))
        res = [x for x, y in sorted(zip(nums,Jumbled_value), key = lambda x:x[1])]
        return res
