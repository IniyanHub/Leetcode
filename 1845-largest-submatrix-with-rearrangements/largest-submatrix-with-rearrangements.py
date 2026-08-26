class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        heights = [0] * n
        answer = 0

        for i in range(m):

            # Calculate consecutive 1s for each column
            for j in range(n):
                if matrix[i][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0

            # IMPORTANT:
            # Don't sort heights directly.
            sorted_heights = sorted(heights, reverse=True)

            # Calculate maximum area
            for j in range(n):
                width = j + 1
                area = sorted_heights[j] * width
                answer = max(answer, area)

        return answer