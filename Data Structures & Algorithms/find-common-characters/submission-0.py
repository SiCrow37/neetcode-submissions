class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        keep = {}
        curr = {}

        for ch in words[0]:
            if ch not in keep:
                keep[ch] = 1
            else:
                keep[ch] += 1

        for i in range(1, len(words)):
            for ch in words[i]:
                if ch in keep:
                    if ch not in curr:
                        curr[ch] = 1
                    elif keep[ch] > curr[ch]:
                        curr[ch] += 1
            keep = curr
            curr = {}

        ans = []
        for ch in keep:
            while keep[ch] > 0:
                ans.append(ch)
                keep[ch] -= 1
        
        return ans
        

                