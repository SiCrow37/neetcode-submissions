class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()
        c_dict = dict()
        for i in s:
            if i in c_dict:
                c_dict[i] += 1
            else:
                c_dict[i] = 1
        
        for j in t:
            if j in c_dict:
                c_dict[j] -= 1
            else:
                return False
            
        for c in c_dict:
            if c_dict[c] != 0: return False
            
        return True
        
        
