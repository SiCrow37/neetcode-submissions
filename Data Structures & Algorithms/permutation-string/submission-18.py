class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # seen hashMap
        d = dict()
        # current length
        cl = 0
        l = len(s1)
        l2 = len(s2)

        for ch in s1:
            if ch not in d:
                d[ch] = 1
                print(f"{ch}: {d[ch]}")
            else:
                d[ch] += 1
                print(f"{ch}: {d[ch]}")
        
        i = 0
        left = 0
        right = 0
        while i < l2:
            c = s2[i]
            if c in d and d[c] > 0:
                cl += 1

                if cl == 1:
                    left = i

                d[c] -= 1

                if cl == l:
                    return True
                i += 1
            elif c in d and d[c] == 0:
                if cl > 0:
                    right = i
                    while cl > 0:
                        i-=1
                        d[s2[i]] += 1
                        cl -= 1
                    i = left + 1 
            else:
                if cl > 0:
                    right = i
                    while cl > 0:
                        i-=1
                        d[s2[i]] += 1
                        cl -= 1
                    i = right
                else:
                    i+=1
        
        return False
            
