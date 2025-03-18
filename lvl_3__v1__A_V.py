# -*- coding: utf-8 -*-

import unittest

def zigzag_mtrx(n, m):
    if n <= 0 or m <= 0:
        return []
    
    mtrx = [[0] * m for _ in range(n)]
    rslt = []
    step = 1 # 9
    
    for diag in range(n + m - 1):
        
        if diag % 2 == 0:

            row = min(diag, n - 1)
            col = diag - row
            
            while row >= 0 and col < m:

                mtrx[row][col] = step
                rslt.append((row, col))

                step += 1 # -
                row -= 1
                col += 1
        else:

            col = min(diag, m - 1)
            row = diag - col
            
            while col >= 0 and row < n:

                mtrx[row][col] = step
                rslt.append((row, col))

                step += 1 # - 
                col -= 1
                row += 1
    
    return mtrx


'''
class TestZigzagMatrix(unittest.TestCase):
    def test_3x3(self):
        expected = [[1, 2, 6],
                    [3, 5, 7],
                    [4, 8, 9]]
        self.assertEqual(zigzag_matrix(3, 3), expected)

'''


print(zigzag_mtrx(3, 3))

#print("_______")
#print(zigzag_mtrx(3, 5))
    

        
if __name__ == "__main__":
    unittest.main()
