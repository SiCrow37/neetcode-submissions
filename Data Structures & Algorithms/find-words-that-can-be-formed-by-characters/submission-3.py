class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        l = ""

        for ch in chars:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
        print(chars)
        print(d)
        print("\n\n\n===== START =====")
        
        for w in words:
            cd = d.copy()
            good = True

            print("\n", w)

            for ch in w:
                if ch in cd:
                    cd[ch] -= 1
                else:
                    good = False
                    print(f"{ch} not in d -> broken")
                    break

            if good == True:
                print(cd)
                for k in cd:
                    if cd[k] < 0:
                        good = False
            
            if good == True:
                l += w
                print(l)
        
        return len(l)
            





