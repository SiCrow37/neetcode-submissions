class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) -1
        low = 0
        mid = 0
        not_found = True
     
        while low <= high:
            mid = low + ((high-low) // 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1 
        return -1
   
# 1=2, 2=3, 3=4, 4=3

