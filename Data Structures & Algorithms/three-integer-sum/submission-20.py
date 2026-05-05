class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = dict()
        my_list = []
        curr_list = []

        for n in nums:
            if n not in seen:
                seen[n] = 1
            else: seen[n] += 1
        
        if 0 in seen and seen[0] == 3:
            my_list.append([0, 0, 0])

        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                one = [nums[0], nums[1], nums[2]]
                one_list = []
                one_list.append(one)
                return one_list
                
        
        for i in range(0, len(nums) - 3):
            a = nums[i]

            for j in range(i + 1, len(nums)):
                b = nums[j]

                c = 0 - (a + b)
                
                if c in seen:

                    if c == b or c == a:
                        if seen[c] == 1:
                            continue
                    if c == b and c == a:
                        if seen[c] < 3:
                            continue

                    curr_list = [a, b, c]

                    curr_list = sorted(curr_list)

                    if curr_list not in my_list:
                        my_list.append(curr_list)
                        curr_list = []
                        a = nums[i]
                    else: 
                        curr_list = []
                        a = nums[i]

        return my_list
            



        
