class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fdict = dict()
        topK = []
        for num in nums:
            if num not in fdict:
                fdict[num] = 1
            else: 
                fdict[num] = fdict[num] + 1
        while len(topK) < k:
            top_val = max(fdict.values())
            for t in fdict:
                if fdict[t] == top_val:
                    topK.append(t)
                    fdict[t] = 0
                    break
        return topK


