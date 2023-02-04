class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort(reverse=True)
        a=[]
        for i in range(len(deck)):
            if len(a)==0:
                a.append(deck[i])
            else:
                a=[a[-1]]+a[:-1]
                a=[deck[i]]+a
        return a