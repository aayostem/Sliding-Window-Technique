import math
from collections import defaultdict
from collections import deque


class Solution:

    def longest_substring_with_k_distinct(self, s: str, k: int) -> int:
        if not s or k <= 0:
            return 0

        char_frequency = {}
        max_length = 0
        window_start = 0

        for window_end in range(len(s)):
            char = s[window_end]
            char_frequency[char] = char_frequency.get(char, 0) + 1

            while len(char_frequency) > k:
                left_char = s[window_start]
                char_frequency[left_char] -= 1
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length
