
# -*- coding: utf-8 -*-

import unittest


def zigzag_sort(mtrx):

    if not mtrx or not mtrx[0]:
        return []
    
    rows = len(mtrx)
    cols = max(len(row) for row in mtrx)

    rslt = []
    
    for diag in range((rows + cols - 2), 0, -1):
        print("___")
        print(diag)
        if diag % 2 == 0:
            print("if")

            row = min(diag, rows - 1)
            col = diag - row

            print("row = ", row)
            print("col = ", col)

            while row >= 0 and col < cols:

                if 0 <= row < rows and 0 <= col < len(mtrx[row]):

                    rslt.append(mtrx[row][col])

                    print(mtrx[row][col])

                row -= 1
                col += 1
        else:
            print("else")

            row = min(diag, cols - 1)
            col = diag - row

            print("row = ", row)
            print("col = ", col)

            while (col >= 0) and (row < rows):

                if 0 <= row < rows and 0 <= col < len(mtrx[row]):

                    rslt.append(mtrx[row][col])

                    print(mtrx[row][col])

                col -= 1
                row -= 1

    return rslt

class TestZigzagTraversal(unittest.TestCase):

    def test_case_1(self):

        mtrx = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        
        #self.assertEqual(zigzag_sort(mtrx), [1, 2, 4, 7, 5, 3, 6, 8, 9])
        print(zigzag_sort(mtrx))

        

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)