class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # Keep dividing n by 3 as long as it is divisible
        while n % 3 == 0:
            n //= 3
            
        # If n is a power of three, we will eventually reach 1
        return n == 1
        