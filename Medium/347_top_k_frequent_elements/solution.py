class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        max_frequency = 0

        for num in nums:  # O(N)
            if count_dict.get(num):
                count_dict[num] += 1
            else:
                count_dict[num] = 1
            if count_dict[num] > max_frequency:
                max_frequency = count_dict[num]

        count_list = [[] for i in range(max_frequency)]

        for num in count_dict.keys():
            count_list[count_dict[num] - 1].append(num)

        final_list = []
        for list_ in count_list:
            final_list += list_

        return final_list[-k:]
