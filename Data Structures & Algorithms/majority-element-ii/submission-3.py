class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        v = len(nums)/3
        d = {}
        ans = []

        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        
        for n in d:
            if d[n] > v:
                ans.append(n)
        
        return ans
