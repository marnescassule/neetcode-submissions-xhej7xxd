class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        idx_start = 0
        idx_end = idx_start + 1
        numbers_hash = {}

        while(idx_start < len(nums)):
            if nums[idx_start] in numbers_hash:
                return numbers_hash[nums[idx_start]] 
            else:
                numbers_hash[nums[idx_start]] = True
            
            idx_start += 1
        return False
        