class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if sentence1 == sentence2:
            return True
        if len(sentence1) != len(sentence2):
            return False
        
        if similarPairs:
            i = 0
            while i < len(sentence1):
                if sentence1[i] == sentence2[i]:
                    i+=1
                    continue
                else:
                    pair1 = [sentence1[i], sentence2[i]]
                    pair2 = [sentence2[i], sentence1[i]]
                    if pair1 not in similarPairs and pair2 not in similarPairs:
                        return False
                    i += 1
            return True
                