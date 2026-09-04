class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in operations:
            if i == "C":
                record.pop()
            elif i == "+":
                val = int(record[-1]) + int(record[-2])
                record.append(val)
            elif i == "D":
                val = int(record[-1]) *2
                record.append(val)
            else:
                record.append(int(i))
        return sum(record)