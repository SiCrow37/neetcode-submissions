class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        candidates = deque()
        results = []

        while i < len(nums):
            
            # while window is maxed, anything outside of window is removed
            while candidates and candidates[0][1] <= i - k:
                candidates.popleft()
            
            # adding new value while removing all smaller values
            while candidates and nums[i] >= candidates[-1][0]:
                candidates.pop()
            candidates.append((nums[i], i))


            if candidates and i >= k - 1:
                results.append(candidates[0][0])

            i += 1

        return results




# while i < len(nums)
# 1. i increments
# 2. if itterator is >= k - 1
#   -> check if farthest left's index is < i - k and remove it if so
# 3. nums[i] ADDED to candidates 
#   -> if larger than largest, remove all
#   -> if smallest, append it
#   -> if larger than smallest and smaller than largest, remove all that are smaller or equal
# 4. if itterator is >= k - 1 
#   -> add far left candidate to results
# 5. return results
