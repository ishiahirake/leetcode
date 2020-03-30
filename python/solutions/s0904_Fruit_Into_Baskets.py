from collections import Counter
from typing import List


class Solution:
    """
    904. Fruit Into Baskets.

    :see https://leetcode.com/problems/fruit-into-baskets/
    """

    def totalFruit(self, tree: List[int]) -> int:
        total_count = li = 0
        counter = Counter()
        for hi, fruit in enumerate(tree):
            counter[fruit] += 1
            while len(counter) > 2:
                old_fruit = tree[li]
                counter[old_fruit] -= 1
                if counter[old_fruit] == 0:
                    del counter[old_fruit]
                li += 1
            total_count = max(total_count, hi - li + 1)
        return total_count
