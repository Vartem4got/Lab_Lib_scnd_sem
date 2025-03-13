# -*- coding: utf-8 -*-


import unittest


def zigzag_sort(mtrx):
    if not mtrx or not mtrx[0]:
        return []
    
    rows = len(mtrx)
    cols = max(len(row) for row in mtrx)

    rslt = []
    
    for diag in range(rows + cols - 1):

        if diag % 2 == 0:

            row = min(diag, rows - 1)
            col = diag - row

            while row >= 0 and col < cols:

                if 0 <= row < rows and 0 <= col < len(mtrx[row]):

                    rslt.append(mtrx[row][col])

                row -= 1
                col += 1
        else:

            col = min(diag, cols - 1)
            row = diag - col

            while col >= 0 and row < rows:

                if 0 <= row < rows and 0 <= col < len(mtrx[row]):

                    rslt.append(mtrx[row][col])

                col -= 1
                row += 1

    return rslt


        # B-T

class TestZigzagTraversal(unittest.TestCase):

    def test_case_1(self):

        mtrx = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12]
        ]

        # works good
        
        self.assertEqual(zigzag_sort(mtrx), [1, 2, 4, 7, 5, 3, 6, 8, 10, 11, 9, 12])

    def test_case_2(self):

        mtrx = [
            [1, 2, 6],
            [3, 5, 9],
            [7, 8, 10],
            [11, 13, 14],
            [15]
        ]

        # yep works to

        self.assertEqual(zigzag_sort(mtrx), [1, 2, 3, 7, 5, 6, 9, 8, 11, 15, 13, 10, 14] )

    def test_single_row(self):

        mtrx = [[1, 2, 3, 4]]

        # 1 row no probl looks good

        self.assertEqual(zigzag_sort(mtrx), [1, 2, 3, 4])

    def test_single_column(self):

        mtrx = [[1], [2], [3], [4]]

        # 1 colm same goes good

        self.assertEqual(zigzag_sort(mtrx), [1, 2, 3, 4])

    def test_empty_matrix(self):

        mtrx = []

        # no numbers no problms

        self.assertEqual(zigzag_sort(mtrx), [])

       
# main main main main

if __name__ == "__main__":
    unittest.main()
