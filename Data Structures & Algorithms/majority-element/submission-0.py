class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements_array = {}

        for ele in nums:
            if ele in elements_array:
                elements_array[ele] += 1
            else:
                elements_array[ele] = 1
        
        majority_number = 0
        
        for key, value in elements_array.items():
            majority_number = max(majority_number, value)
            if(majority_number == value):
                element_major = key
        
        return element_major
        