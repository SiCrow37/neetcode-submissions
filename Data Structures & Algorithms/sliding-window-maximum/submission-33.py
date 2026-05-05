class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        window = deque()
        results = []

        while i < k:
            window.append(nums[i])
            i += 1

        # i == 3 at start
        while i < len(nums) + 1:
            results.append(max(window))

            # find a more efficient way than using max()... keep track of largest

            if i <= len(nums) - 1:
                window.append(nums[i])
                window.popleft()

            i += 1

        return results




        