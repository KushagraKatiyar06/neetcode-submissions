class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import collections
        # Using defaultdict(set) ensures rows[r] creates a set if it doesn't exist
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                val = board[r][c]
                box_key = (r // 3, c // 3)

                if (val in rows[r] or
                    val in columns[c] or
                    val in squares[box_key]):
                    return False
                
                rows[r].add(val)
                columns[c].add(val)
                squares[box_key].add(val)

        return True