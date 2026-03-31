class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        idx = 0

        while(idx < len(nums)):
            if(nums[idx] != val):
                nums[k]=nums[idx]
                k+=1
            idx+=1
        return k
