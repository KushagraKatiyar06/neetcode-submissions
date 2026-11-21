class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen_in_row = {} #key is the index in horizontal array -> value is []
        seen_in_column = {} #key is index of column -> value is []
        seen_in_box = {} #key is index of box using mods for x,y coordinate -> value is []

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                if row not in seen_in_row:
                    seen_in_row[row] = set()
                if col not in seen_in_column:
                    seen_in_column[col] = set()
                if (row//3, col//3) not in seen_in_box:
                    seen_in_box[(row//3, col//3)] = set()

                if board[row][col] in seen_in_row[row] or board[row][col] in seen_in_column[col] or board[row][col] in seen_in_box[(row//3,col//3)]:
                    return False
                else:
                    seen_in_row[row].add(board[row][col])
                    seen_in_column[col].add(board[row][col])
                    seen_in_box[(row//3, col//3)].add(board[row][col])

        return True