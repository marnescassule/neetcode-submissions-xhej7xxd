class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        uniques = [num for num, count in counts.items() if count == 1]
        return max(uniques) if uniques else -1


        