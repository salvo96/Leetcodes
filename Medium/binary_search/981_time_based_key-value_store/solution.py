class TimeMap:
    def __init__(self):
        self.memory = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.memory.get(key):
            self.memory[key] = []
        self.memory[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        memory_lst = self.memory.get(key)

        if not memory_lst:
            return ""

        left, right = 0, len(memory_lst) - 1
        while left <= right:
            middle = (left + right) // 2

            if timestamp == memory_lst[middle][1]:
                return memory_lst[middle][0]
            elif timestamp < memory_lst[middle][1]:
                right = middle - 1
            else:
                left = middle + 1

        if right < 0:
            return ""
        return memory_lst[left][0] if right > left else memory_lst[right][0]
