class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        major = []
        items_array = {}

        for ele in nums:
            if ele in items_array:
                items_array[ele] += 1
            else:
                items_array[ele] = 1
        
        for key, value in items_array.items():
            if(items_array[key] > len(nums)//3):
                major.append(key)

        return major


        