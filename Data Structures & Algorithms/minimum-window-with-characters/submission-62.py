class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # normalize values
        # minimum value tracker
        # current window size tracker
        # valid window bool
        # left and right dynamic window pointers
        # LOOP WHILE -> (len(s) - 1 - left pointer) >= minimum value
        # next start window position tracker 
        #   - increments to next valid character past the current left pointer 
        #   - increments when length of current window size > minimum value
        #   - OR when right pointer reaches the length of s and current window is not valid
        #   - OR when the current window is validated
        # WHEN left pointer increments, right pointer must be reset to left pointer + 1

        if t in s or t == s:
            return t

        s = list(s)
        t = list(t)
        ls = len(s)
        lt = len(t)
        td = dict()
        seen = dict()
        minimum = -1
        curr = ""
        left = 0
        right = 0
        next_left = -1
        result = ""
        counter = 1

        for ch in t:
            if ch not in td:
                td[ch] = 1
            else: td[ch] += 1

        if lt > ls:
            return ""

        if lt == ls:
            for ch in s:
                if ch not in seen:
                    seen[ch] = 1
                else:
                    seen[ch] += 1
            if seen == td:

                for ch in s:
                    result += ch
                return result
            else:
                return ""


        else:
            while ls - left > lt:
                print(f"\n<<<<  Round {counter}  >>>>")
                counter += 1
                print(f"left: {left}    right: {right}")

                if s[left] not in td:
                    print("item skipped")
                    left += 1
                    print(left)

                else:
                    if curr == "":
                        print("current: \"\"")
                        # every time left is set, seen automatically has its first value
                        seen[s[left]] = 1
                        # concat left value to curr for first value
                        curr += s[left]
                        print(f"current: {curr}")

                        # update right pointer when left is set
                        if left+1 < ls - 1 and len(curr) == 1:
                            right = left+1
                            print(f"right: {right}")
                            print(curr)

                    if s[right] in td and s[right] not in seen:
                        seen[s[right]] = 1
                        print(seen)
                        curr += s[right]
                        print(curr)
                        print(curr)
                        if next_left == -1:
                            next_left = right
                            print(f"next left: {right}")
                        right += 1

                    elif s[right] in td and s[right] in seen:
                        if seen[s[right]] < td[s[right]]:
                            seen[s[right]] += 1
                            print(seen)
                        curr += s[right]
                        print(curr)
                        if next_left == -1:
                            next_left = right
                            print(f"next left: {right}")
                        right += 1

                    elif s[right] not in td:
                        curr += s[right]
                        print(curr)
                        right += 1
                    
                    if td == seen:
                        print("!!!MATCH!!!")
                        print(seen)
                        print(td)
                        seen = dict()
                        print("seen reset:")
                        print(seen)
                        if minimum == -1:
                            minimum = len(curr)
                            result = curr
                            print(f"FIRST result: {result}")
                            print(f"curr: {curr}")
                        
                        elif minimum != -1 and len(curr) < minimum:
                            result = curr
                            print(f"result: {result}")
                            minimum = len(curr)
                        
                        curr = ""
                        print("curr RESET")
                        
                        if next_left == -1:
                            print(f"next left == -1, incremented by 1")
                            left += 1
                        else:
                            print(f"left switched to next_left and next_left reset to -1")
                            left = next_left
                            print(f"new left: {left}")
                            next_left = -1
                            right = left+1
                    
                    elif right == ls and td != seen and minimum == -1:
                        print("end 1")
                        return ""
                    elif right == ls and td != seen and minimum != -1:
                        print("end 2")
                        return result
                

        return result

                    
                        


