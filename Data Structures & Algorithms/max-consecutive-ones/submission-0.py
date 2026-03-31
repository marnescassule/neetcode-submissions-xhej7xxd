class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_one = 0
        temp_one = 0

        for idx in range(len(nums)):
            if(nums[idx] == 1):
                temp_one +=1
            else:
                if(temp_one > count_one):
                    count_one = temp_one
                
                temp_one = 0
            if(temp_one > count_one):
                count_one = temp_one
        
        return count_one