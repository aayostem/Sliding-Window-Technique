import math
from collections import defaultdict
from collections import deque


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_length = 0
        window_start = 0

        for window_end in range(len(s)):
            char = s[window_end]

            while char in char_set:
                char_set.remove(s[window_start])
                window_start += 1

            char_set.add(char)

            max_length = max(max_length, window_end - window_start + 1)
        return max_length
