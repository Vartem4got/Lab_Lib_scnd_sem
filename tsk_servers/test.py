import unittest
from main_task import find_optimal_server, counting

class Test(unittest.TestCase):
    def test_count(self):
        graph = [
            [],
            [(2, 1)],
            [(1, 1), (3, 1)],
            [(2, 1)],
        ]
        n = 3
        result = counting(1, n, graph)
        self.assertEqual(result[3], 2)

    def test_find_optimal_server(self):
        n = 4
        users = {2, 4}
        graph = [
            [],
            [(2, 1), (3, 2)],
            [(1, 1), (4, 2)],
            [(1, 2), (4, 1)],
            [(2, 2), (3, 1)],
        ]
        result = find_optimal_server(n, users, graph)
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
