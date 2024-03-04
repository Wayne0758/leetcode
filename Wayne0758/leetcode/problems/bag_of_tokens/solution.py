class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score=0
        scoretemp=0
        while tokens:
            if tokens[0]>power:
                if score==0:
                    return 0
                else:
                    scoretemp=score
                    score-=1
                    power+=tokens.pop(-1)
            else:
                power-=tokens.pop(0)
                score+=1
        return max(score,scoretemp)