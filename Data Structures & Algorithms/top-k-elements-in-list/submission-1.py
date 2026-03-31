class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        list_frequent_elements = []
        numbers = {}
        buckets=[[] for _ in range(len(nums) +1)]

        for ele in nums:
            if ele in numbers:
                numbers[ele]+=1
            else:
                numbers[ele]=1
        
        count_elements = 0

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in numbers.items():
            buckets[freq].append(num)
        
        result = []
        for idx in range(len(buckets) -1, 0, -1):
            for num in buckets[idx]:
                result.append(num)
                if len(result) == k: 
                    return result
        

        

        