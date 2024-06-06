class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        while hand:
            a=hand.pop(0)
            for i in range(1,groupSize):
                if (a+i) in hand:
                    hand.remove(a+i)
                else:
                    return False
        return True
