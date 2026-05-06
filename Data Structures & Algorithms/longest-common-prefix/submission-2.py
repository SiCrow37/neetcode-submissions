class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        j = 0
        pre = ""
        
        while i < len(strs[0]):
            for s in strs:
                if len(s) <= i:
                    return pre
                if s[i] != strs[0][i]:
                    return pre
            pre += strs[0][i]
            i += 1
        return pre

            

