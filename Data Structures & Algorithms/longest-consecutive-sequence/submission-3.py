class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = dict()
        curr = 0
        longest = 0

        for num in nums:
            if num not in seen:
                seen[num] = 1

        for num in seen:
            curr = 1
            i = 1
            if num + 1 not in seen:
                while num - i in seen:
                    curr += 1
                    i += 1

                if curr > longest:
                    longest = curr
            if num - 1 not in seen:
                while num + i in seen:
                    curr += 1
                    i += 1
                if curr > longest:
                    longest = curr

        return longest
                
            