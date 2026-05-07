class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for w in words:
            for j in words:
                if w in j and w not in ans and j != w:
                    ans.append(w)

        return ans