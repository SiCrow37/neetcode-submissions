class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = dict()
        i = -1
        vals = [0, 0]
        for ch in nums:
            i += 1
            if ch in my_dict:
                vals[0] = my_dict[ch]
                vals[1] = i
                return vals
            else:
                my_dict[target - ch] = i
            
            