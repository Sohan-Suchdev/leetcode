class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0])*len(matrix)-1

        while l <= r:
            mid = (l + r) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True
        return False