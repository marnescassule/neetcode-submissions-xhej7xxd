class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stackStore = []
        for op in operations:
            if op == "C":
                stackStore.pop()
            elif op == "D":
                stackStore.append(stackStore[-1] * 2)
            elif op == "+":
                stackStore.append(stackStore[-1] + stackStore[-2])
            else:
                stackStore.append(int(op))
        return sum(stackStore)
        