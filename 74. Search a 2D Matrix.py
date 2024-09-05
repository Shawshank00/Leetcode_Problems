class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)     #Number of row
        n = len(matrix[0])  #Number of columns
        t = m * n           #Total elements in 2D array

        L, R = 0, t - 1

        while L <= R:
            M = (L + R) // 2
            i = M // n      #Row position
            j = M % n       #column position

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                L = M + 1
            else:
                R = R - 1
        return False

        #TC - O(log n)
        #SC - O(1)


