class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        i = 0

        if len(nums) == 1:
            return True

        for i in range(len(nums)):
            if nums[0]%2==1:
                if i % 2 == 0:
                    if nums[i] %2 != 1:
                        return False
                if i%2==1:
                    if nums[i]%2!=0:
                        return False

            if nums[0]%2==0:
                if i%2==0:
                    if nums[i]%2!=0:
                        return False
                if i%2==1:
                    if nums[i]%2!=1:
                        return False
        return True


