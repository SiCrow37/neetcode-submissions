class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        d = {}
        start = 0
        count = 0

        s = list(s)
        pattern = list(pattern)

        for ch in s: 
            if ch == ' ':
                count += 1
        if count >= len(pattern):
            return False
        if pattern == s:
            return False
        if count == 0 and len(pattern) > 1:
            return False

        for p in pattern:
            print(f"\np = {p}")
            curr = ""
            for i in range(start, len(s)):
                print(f"  i = {i}")
                if s[i].isalpha():
                    curr += s[i]

                if s[i] == ' ':
                    if p not in d:
                        d[p] = curr
                        start = i + 1
                        break
                    elif curr != d[p]:
                        print("here")
                        return False
                    else:
                        start = i + 1
                        break

                if i == len(s) - 1:
                    print("here here")
                    if p not in d and curr in d.values():
                        return False
                    elif p in d and curr not in d.values():
                        return False
                
        return True
                    
                        

                


        

                    
