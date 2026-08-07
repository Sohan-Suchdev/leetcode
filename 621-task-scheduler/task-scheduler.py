class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = collections.Counter(tasks)
        max_freq = max(freq.values())
        max_freq_count = sum(1 for count in freq.values() if count == max_freq)
        calculated_time = (max_freq - 1) * (n + 1) + max_freq_count
        return max(len(tasks), calculated_time)