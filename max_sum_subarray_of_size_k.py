import math
from collections import defaultdict
from collections import deque


class Solution:

    def max_sum_subarray_of_size_k(self, arr: list[int], k: int) -> int:
        if not arr or k <= 0 or k > len(arr):
            return 0

        max_sum = 0
        window_sum = 0
        window_start = 0

        for window_end in range(len(arr)):
            window_sum += arr[window_end]

            if window_end >= k - 1:
                max_sum = max(max_sum, window_sum)
                window_sum -= arr[window_start]
                window_start += 1

        return max_sum
