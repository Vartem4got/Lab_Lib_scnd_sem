# -*- coding: utf-8 -*-

import unittest

def max_hamsters(S, C, hamsters):
    hamsters.sort(key=lambda x: x[0] + x[1])
    
    def can_feed(count):
        total_food = 0
        for i in range(count):
            total_food += hamsters[i][0] + hamsters[i][1] * (count - 1)
            if total_food > S:
                return False
        return True
    
    left, right = 0, C
    while left < right:
        mid = (left + right + 1) // 2
        if can_feed(mid):
            left = mid
        else:
            right = mid - 1
    
    return left

class TestHamsters(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(max_hamsters(7, 3, [[1, 2], [2, 2], [3, 1]]), 2)
        self.assertEqual(max_hamsters(19, 4, [[5, 0], [2, 2], [1, 4], [5, 1]]), 2)
        self.assertEqual(max_hamsters(2, 2, [[1, 50000], [1, 60000]]), 1)

if __name__ == "__main__":
    unittest.main()
