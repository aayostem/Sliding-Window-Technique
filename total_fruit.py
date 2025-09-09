import math
from collections import defaultdict
from collections import deque


class Solution:

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
