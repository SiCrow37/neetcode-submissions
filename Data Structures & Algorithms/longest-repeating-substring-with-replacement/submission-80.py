class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # max window
        m = 0
        #left pointer
        l = 0
        # next left side of window
        n = -1
        # right pointer
        r = 1
        # changeable k val
        j = k
        # length
        length = len(s)
        # current length of substring
        c = 0

        if len(s) == 1:
            return 1

        s = list(s)

        c += 1

        counter = 1


################# CHECKING THE END first
        r = -1
        l = length - 2
        c = 0
        c += 1
        j = k
        while l > 0 and j > 0:
            if s[r] == s[l]:
                c += 1
                if c > m:
                    m = c
                l -= 1
            
            elif s[r] != s[l]:
                j -= 1
                c += 1
                l -= 1
                if c > m:
                    m = c
################

        n = -1
        c = 1
        j = k
        r = 1
        l = 0

        print("While loop start >>>")
        while r < length:
            counter += 1

            if s[r] == s[l]:
                c += 1
                r += 1
                if c > m:
                    m = c

            elif s[r] != s[l] and j > 0:
                if n == -1:
                    n = r
                c += 1
                r += 1
                j -= 1
                if c > m:
                    m = c

                # PLEASE!
                if r == length and n > -1 and j == 0:
                    l = n
                    n = -1

                    j = k

                    r = l + 1
                    c = 0
                    c += 1
                    if c > m:
                        m = c
                
             
            
            elif s[r] != s[l] and j == 0:
                if c > m:
                    m = c

                c = 0
                j = k

                if n > -1:
                    l = n
                    r = l + 1
                    n = -1
               
                else:
                    l = r
                    r = l + 1

                c += 1
            

        counter = 1
        if r == length and j > 0:
            while l > 0:
                counter+=1

                l -= 1
                if s[l] != s[l+1] and j > 0:
                    s[l] = s[l+1]
                    c += 1
                    j -= 1
                    if c > m:
                        m = c
                    if j == 0:
                        break
                elif s[l] == s[l+1]:
                    c += 1
                    if c > m:
                        m = c

        return m







