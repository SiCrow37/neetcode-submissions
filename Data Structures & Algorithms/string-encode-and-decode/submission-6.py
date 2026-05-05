class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code = code + s + "-"
        return code


    def decode(self, s: str) -> List[str]:
        strs = []
        curr_word = ""
        for ch in s:
            if ch == '-':
                strs.append(curr_word)
                curr_word = ""
            else:
                curr_word = curr_word + ch
        return strs
