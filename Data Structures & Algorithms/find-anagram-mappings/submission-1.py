class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        dict_nums = {}

        for idx in range(len(nums2)):
            dict_nums[nums2[idx]] = idx


        for idx in range(len(nums1)):
            result.append(dict_nums[nums1[idx]])
        
        return result