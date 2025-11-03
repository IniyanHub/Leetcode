class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0] or not word:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(r, c, index):
            # Base case 1: Out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            
            # Base case 2: Character mismatch
            if board[r][c] != word[index]:
                return False

            # Base case 3: Word found
            if index == len(word) - 1:
                return True

            # Mark the cell as visited to prevent reuse
            temp = board[r][c]
            board[r][c] = '#' 

            # Explore neighbors (up, down, left, right)
            found = (dfs(r + 1, c, index + 1) or
                    dfs(r - 1, c, index + 1) or
                    dfs(r, c + 1, index + 1) or
                    dfs(r, c - 1, index + 1))

            # Backtrack: restore the original value
            board[r][c] = temp
            
            return found

        # Iterate through all cells to start the search
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False