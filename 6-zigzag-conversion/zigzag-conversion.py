class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

    # Create a list of strings to store the characters for each row.
        rows = [''] * numRows
    
    # current_row keeps track of the row we are writing to.
        current_row = 0
    
    # going_down is a flag to track our direction (down or up).
        going_down = False

    # Iterate through each character in the string.
        for char in s:
        # Add the character to the current row.
            rows[current_row] += char
        
        # If we are at the top or bottom row, we need to change direction.
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
        # Move to the next row based on the current direction.
            current_row += 1 if going_down else -1
        
    # Join all the rows to form the final string.
        return "".join(rows)

        