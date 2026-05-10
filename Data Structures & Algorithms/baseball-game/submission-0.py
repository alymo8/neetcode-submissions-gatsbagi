class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total = 0
        for op in operations:
            if op == "+":
                sum_items = record[-1] + record[-2]
                record.append(sum_items)
                total += sum_items
            elif op == "C":
                total -= record[-1]
                record.pop(-1)
            elif op == "D":
                record.append(record[-1] * 2)
                total += record[-1]
            else:
                record.append(int(op))
                total += int(op)
        return total
