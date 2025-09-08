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

    def total_fruit(self, fruits: list[int]) -> int:
        if not fruits:
            return 0

        fruit_frequency = {}
        max_fruits = 0
        window_start = 0

        for window_end in range(len(fruits)):
            fruit = fruits[window_end]
            fruit_frequency[fruit] = fruit_frequency.get(fruit, 0) + 1

            while len(fruit_frequency) > 2:
                left_fruit = fruits[window_start]
                fruit_frequency[left_fruit] -= 1
                if fruit_frequency[left_fruit] == 0:
                    del fruit_frequency[left_fruit]
                window_start += 1

            max_fruits = max(max_fruits, window_end - window_start + 1)

        return max_fruits

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
