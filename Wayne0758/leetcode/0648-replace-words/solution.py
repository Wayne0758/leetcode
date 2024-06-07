class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(' ')
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][:(j+1)] in dictionary:
                    words[i] = words[i][:(j+1)]
                    break
        return ' '.join(words)
