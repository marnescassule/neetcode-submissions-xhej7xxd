class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        numbers_in_array = {}
        good_pairs = 0
        for ele in nums:
            if ele in numbers_in_array:
                numbers_in_array[ele] += 1
            else:
                numbers_in_array[ele] = 1
        
        for key, value in numbers_in_array.items():
            if(value > 1):
                good_pairs = good_pairs + (value * (value - 1))//2
        
        return good_pairs