import heapq
from collections import deque


class Task:
    def __init__(self, name, freq):
        self.name = name
        self.freq = freq

    def __lt__(self, other):
        if self.freq > other.freq:
            return True
        elif self.freq == other.freq:
            if self.name > other.name:
                return True
        return False


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_freq = dict()
        for task in tasks:
            if tasks_freq.get(task):
                tasks_freq[task] += 1
            else:
                tasks_freq[task] = 1

        heap_tasks = [Task(key, value) for key, value in tasks_freq.items()]
        heapq.heapify(heap_tasks)

        counter = 0
        final_tasks = {}
        cooldown = deque()

        while heap_tasks or cooldown:
            while cooldown and cooldown[0][1] <= counter:
                heapq.heappush(heap_tasks, cooldown.popleft()[0])

            if heap_tasks:
                task = heapq.heappop(heap_tasks)

                final_tasks[task.name] = counter
                task.freq -= 1

                if task.freq > 0:
                    cooldown.append((task, counter + n + 1))
            counter += 1

        return counter
