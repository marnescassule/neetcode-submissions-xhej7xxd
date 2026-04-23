class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for idx in range(len(temperatures)):
            while stack and temperatures[idx] > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = idx - prev_idx
            stack.append(idx)
            
        return result