class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        d = {}

        for s in strings:
            
            if len(s) == 1:
                k = (0)
            
            else:
                k = []

                for i in range(1, len(s)):
                    diff = (ord(s[i]) - ord(s[i-1])) % 26
                    k.append(diff)
                
                k = tuple(k)

            if k not in d:
                d[k] = []

            d[k].append(s)
     
        return list(d.values())
