from collections import deque

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        def dfs(row, col, idx, visited):
            if idx == len(word)-1:
                return True

            for i in range(4):
                _row = row + dr[i]
                _col = col + dc[i]
                _idx = idx + 1
                if (
                    _row >= 0 and _row < len(board) and
                    _col >= 0 and _col < len(board[0]) and
                    (_row, _col) not in visited and
                    board[_row][_col] == word[_idx]
                    ):
                    visited.add((_row, _col))
                    if dfs(_row, _col, _idx, visited):
                        return True
                    visited.remove((_row, _col))
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set([(r,c)])):
                        return True79
