class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        w = wordsDict

        w1 = [i for i in range(len(wordsDict)) if wordsDict[i] == word1]
        w2 = [i for i in range(len(wordsDict)) if wordsDict[i] == word2]

        a = 1000000

        for i in w1:
            for j in w2:
                if abs(j - i) < a:
                    a = abs(j-i)
        
        return a





     
                