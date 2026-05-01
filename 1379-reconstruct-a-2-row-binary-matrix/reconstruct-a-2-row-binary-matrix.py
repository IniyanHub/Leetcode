class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
    
        upper_row = [0] * n
        lower_row = [0] * n
    
    # Step 1: Handle colsum = 2
        for i in range(n):
            if colsum[i] == 2:
                upper_row[i] = 1
                lower_row[i] = 1
                upper -= 1
                lower -= 1
    
    # Step 2: Handle colsum = 1
        for i in range(n):
            if colsum[i] == 1:
                if upper > 0:
                    upper_row[i] = 1
                    upper -= 1
                else:
                    lower_row[i] = 1
                    lower -= 1
    
    # Step 3: Check validity
        if upper != 0 or lower != 0:
            return []
    
        return [upper_row, lower_row]
        