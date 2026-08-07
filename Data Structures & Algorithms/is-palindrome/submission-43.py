class Solution:
    def isPalindrome(self, s: str) -> bool:
        il = 0
        ir = len(s)-1

        if len(s) < 1:
            return False
        elif len(s) == 1:
            return True
        elif len(s) == 2:
            if s[il].isalnum() and s[ir].isalnum():
                return s[il].lower() == s[ir].lower()
            if s[il].isalnum() and not s[ir].isalnum():
                return True
            if not s[il].isalnum() and s[ir].isalnum():
                return True
        else:
            while il < ir:
                while not s[il].isalnum() and il < ir:
                    il += 1
                while not s[ir].isalnum() and ir > il:
                    ir -= 1
                if s[il].lower() != s[ir].lower():
                    return False
                il += 1
                ir -= 1

        return True