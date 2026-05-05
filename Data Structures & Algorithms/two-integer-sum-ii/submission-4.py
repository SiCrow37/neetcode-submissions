class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        candidates = dict()
        ans = []
        i = 0
        for n in numbers:
            
            if candidates and n in candidates:
                ans.append(candidates[n])
                ans.append(i + 1)
                if len(ans) == target:
                    break
            else:
                candidates[target - n] = i + 1
            i+=1
        return ans