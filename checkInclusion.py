import math
from collections import defaultdict
from collections import deque


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pattern_map = defaultdict(int)
        for char in s1:
            pattern_map[char] += 1

        matched = 0
        window_start = 0

        for window_end in range(len(s2)):
            right_char = s2[window_end]

            if right_char in pattern_map:
                pattern_map[right_char] -= 1
                if pattern_map[right_char] == 0:
                    matched += 1

            if matched == len(pattern_map):
                return True

            if window_end >= len(s1) - 1:
                left_char = s2[window_start]
                window_start += 1

                if left_char in pattern_map:
                    if pattern_map[left_char] == 0:
                        matched -= 1
                    pattern_map[left_char] += 1

        return False
