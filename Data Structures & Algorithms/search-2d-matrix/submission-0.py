class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        low = 0
        high = len(matrix) * len(matrix[0]) - 1

        while low <= high:
            midpoint = (low + high) // 2
            
            midpoint_y = midpoint % len(matrix[0])
            midpoint_x = (midpoint - midpoint_y) // (len(matrix[0]))

            if matrix[midpoint_x][midpoint_y] == target:
                return True
            elif matrix[midpoint_x][midpoint_y] < target:
                low = midpoint + 1
            elif matrix[midpoint_x][midpoint_y] > target:
                high = midpoint - 1

        return False
        