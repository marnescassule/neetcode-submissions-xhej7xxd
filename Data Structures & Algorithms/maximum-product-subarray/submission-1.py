class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minEnding = nums[0]
        maxEnding = nums[0]

        if(len(nums) == 1):
            return res

        for idx in range(1, len(nums)):
            temp = maxEnding
            maxEnding = max(maxEnding * nums[idx], minEnding * nums[idx], nums[idx])
            minEnding = min(temp * nums[idx], minEnding * nums[idx], nums[idx])

            res = max(res, maxEnding)
        
        return res