class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set()
        max_count = 0

        for num in nums:
            nums_set.add(num)

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            else:
                counter = 1
                current_num = num
                while True:
                    if current_num + 1 in nums_set:
                        counter += 1
                        current_num += 1
                    else:
                        break
                max_count = max(counter, max_count)
        return max_count
