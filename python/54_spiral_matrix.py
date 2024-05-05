class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        r, c = len(matrix), len(matrix[0])

        # Directions for spiraling: right, down, left, up 
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        row, col = 0, 0  
        cur_dir = 0  

        visited = set()

        for _ in range(r * c):
            output.append(matrix[row][col])
            visited.add((row, col))

            next_row = row + dr[cur_dir]
            next_col = col + dc[cur_dir]

            # If the next cell is out of bounds or has been visited
            if (next_row < 0 or next_row >= r or 
                next_col < 0 or next_col >= c or 
                (next_row, next_col) in visited):
                # Change direction
                cur_dir = (cur_dir + 1) % 4

            # Move to the next valid position
            row += dr[cur_dir]
            col += dc[cur_dir]

        return output
