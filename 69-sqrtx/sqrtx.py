class Solution:
    def mySqrt(self, x: int) -> int:

        if x < 2:
            return x

        # Initialize the search boundaries for binary search.
        left, right = 1, x // 2  # The sqrt of x is at most x/2 for x > 1.

        # Perform binary search.
        while left <= right:
            # Calculate the middle point to avoid potential overflow.
            mid = left + (right - left) // 2
            
            # Calculate the square of the middle point.
            # In Python, integers have arbitrary precision, so mid*mid won't overflow.
            # In other languages like C++/Java, you'd need to use a larger type
            # or check `mid > x / mid` to prevent overflow.
            square = mid * mid

            if square == x:
                # Found the exact square root.
                return mid
            elif square < x:
                # The current mid is a potential answer, but a larger one might exist.
                # Discard the left half and search in the right.
                left = mid + 1
            else:  # square > x
                # The current mid is too large.
                # Discard the right half and search in the left.
                right = mid - 1
        
        # When the loop terminates, `right` is the largest integer
        # whose square is less than or equal to x.
        return right
