class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = 0
        for idx in range(len(nums)):
            if(nums[idx-count] == 0):
                x = nums.pop(idx-count)
                nums.append(x)
                count += 1

        return nums
