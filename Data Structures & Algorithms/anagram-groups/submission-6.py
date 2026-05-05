class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = dict()
        if strs:
            for word in strs:
                key = [0] * 26
                if len(word) == 0:
                    key = str(key)
                    if key not in groups:
                        groups[key] = []
                    groups[key].append(word)
                else:
                    for ch in word:
                        key[ord(ch) - ord('a')] += 1
                    key = str(key)
                    if key not in groups:
                        groups[key] = []
                        groups[key].append(word)
                    else: 
                        groups[key].append(word)

        return list(groups.values())
                    
                    
                    
                


            



            

