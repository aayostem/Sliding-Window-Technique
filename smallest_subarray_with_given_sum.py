import math
from collections import defaultdict
from collections import deque


class Solution:

    def smallest_subarray_with_given_sum(self, s: int, arr: list[int]) -> int:
        min_length = math.inf
        window_sum = 0
        window_start = 0

        for window_end in range(len(arr)):
            window_sum += arr[window_end]

            while window_sum >= s:
                min_length = min(min_length, window_end - window_start + 1)
                window_sum -= arr[window_start]
                window_start += 1

        if min_length == math.inf:
            return 0

        return min_length
