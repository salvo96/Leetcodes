import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = dict()
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        word_freq_queue = []
        for word, frequency in word_freq.items():
            heapq.heappush_max(word_freq_queue, (-frequency, word))

            if len(word_freq_queue) > k:
                heapq.heappop_max(word_freq_queue)

        output = k * [""]
        while k > 0:
            output[k - 1] = heapq.heappop_max(word_freq_queue)[1]
            k -= 1

        return output
