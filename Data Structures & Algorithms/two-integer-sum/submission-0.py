class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_hash = {}

        for idx in range(len(nums)):
            if(target - nums[idx] in sum_hash):
                return [sum_hash[target-nums[idx]], idx]
            else:
                sum_hash[nums[idx]] = idx