class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        bucket = [[] for _ in range(len(nums) + 1)]

        for elem in range(len(nums)):
            bucket[nums[elem]].append(elem)
        
        for idx in range(len(bucket)):
            if(len(bucket[idx]) == 0):
                return idx