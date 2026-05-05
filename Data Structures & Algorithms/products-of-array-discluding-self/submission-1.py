class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # build prefix array
        pre = []
        i = 2
        pre.append(1)
        pre.append(nums[0])
        while i < len(nums):
            pre.append(pre[i - 1] * nums[i - 1])
            i+=1

        # build suffix array
        suf = deque()
        i = -3
        suf.append(1)
        suf.appendleft(nums[-1])
        while len(suf) < len(nums):
            suf.appendleft(suf[0] * nums[i + 1])
            i-=1
        suf = list(suf)

        # multiply each index of pre by the same index of suf for get your final array :)
        i = 0
        while i < len(pre):
            pre[i] *= suf[i]
            i+=1
        
        return pre