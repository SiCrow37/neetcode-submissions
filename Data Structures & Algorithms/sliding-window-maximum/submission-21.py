class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # until right pointer is at len(nums)-1

        # left pointer
        # start at 0 

        # right pointer 
        # start at nums[k-1]

        # window = append from left to right

        # search for max in window 

        # increment left and right pointers by 1
        # append next value to window 
        # popleft() value from window
        
        i = 0

        window = deque()
        results = []

        while i < k:
            window.append(nums[i])
            i += 1
        # i == 3 now

        while i < len(nums) + 1:
            m = -10001

            # append max of current window
            for item in window:
                if item > m:
                    m = item
            results.append(m)

            # append new value nums[i] 
            # popleft() leftmost value from window
            if i <= len(nums) - 1:
                window.append(nums[i])
                window.popleft()

            i += 1

        return results




        