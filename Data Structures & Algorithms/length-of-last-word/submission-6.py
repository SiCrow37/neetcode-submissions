class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = -1
        ss = 0
        
        if s[i] == ' ':
            while s[i] == ' ':
                i -= 1
        
        ss = 1
        i -= 1
        while len(s) + i > 0 and s[i].isalpha():
            i -= 1
            ss += 1
        
        return ss
        

