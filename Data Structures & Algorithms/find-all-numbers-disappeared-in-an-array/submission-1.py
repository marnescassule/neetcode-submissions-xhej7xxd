class Solution:
    def findDisappearedNumbers(self, nums):
        set_nums = set(nums)
        numbers = [x for x in range(1,len(nums) +1) if x not in nums]

        return numbers
