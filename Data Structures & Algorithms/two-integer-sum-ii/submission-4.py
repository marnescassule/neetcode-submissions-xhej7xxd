class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx = 0
        idx2 = len(numbers) -1

        while(idx2 < len(numbers)):
            if(numbers[idx] + numbers[idx2] == target):
                return [idx+1, idx2+1]
            else:
                if(numbers[idx] + numbers[idx2] > target):
                    idx2 -= 1
                 
                else:
                    idx += 1