class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_info = [(p, s) for p, s in zip(position, speed)]
        car_info.sort(reverse=True)

        stack = []
        for info in car_info:
            position = info[0]
            speed = info[1]
            time = (target - position) / speed

            if stack:
                if stack[-1] < time:
                    stack.append(time)
            else:
                stack.append(time)
        return len(stack)
