class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        row, column = 0, 0

        while target > matrix[row][-1]:
            row += 1
        while target > matrix[row][column]:
            column += 1

        if target == matrix[row][column]:
            return True
        if target > matrix[row][column - 1] and target < matrix[row][column]:
            return False

        return False
