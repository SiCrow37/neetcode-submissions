class Solution:
    def specialArray(self, nums: List[int]) -> int:

        nums.sort()

        d = defaultdict(int)

        m = -1

        for n in nums:
            d[n] += 1
        
        for i in range(1, len(nums)+1):
            print(f"i -> {i}")
            count = 0
            for k in d:
                if k >= i:
                    count += d[k]
                    print(count)
            if count == i:
                m = i

        return m

            

        

