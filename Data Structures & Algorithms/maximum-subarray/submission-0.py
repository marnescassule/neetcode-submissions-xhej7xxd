class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxValue = nums[0]

        max_ending = maxValue
        for i in range(1, len(nums)):
            max_ending = max(max_ending + nums[i], nums[i])

            maxValue = max(maxValue, max_ending)
        
        return maxValue

        