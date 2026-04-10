class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
      
        comparison = "none"

        for idx in range(1, len(nums)):
            if (comparison == "none"):
                if(nums[idx-1] > nums[idx]):
                    comparison = "more"
                elif(nums[idx-1] < nums[idx]):
                    comparison = "less"
            else:
                if nums[idx-1] > nums[idx] and comparison == "less":
                    return False
                if nums[idx-1] < nums[idx] and comparison == "more":
                    return False
                

        return True
