class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = dict()
        for num in nums:
            if num not in count:
                count[num] = 1
            else: count[num] = count[num]+1
    
        i = 0
        while len(count) > 0:

            m = 101
            c = 0

            for n in count:
                if count[n] < m:
                    m = count[n]
                    c = n
                if count[n] == m:
                    if n > c:
                        m = count[n]
                        c = n
            
            while m > 0:
                nums[i] = c
                i += 1
                m -= 1
            
            del count[c]

        return nums

            
        
            