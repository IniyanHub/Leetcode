class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        # Handle negative exponents
        # x^-n is equivalent to 1 / x^n
        if n < 0:
            x = 1 / x
            n = -n
            
        result = 1.0
        current_product = x
        
        # Iterate while there is still power to compute
        while n > 0:
            # If n is odd, multiply the current product into the result
            # We use bitwise AND to check if the least significant bit is 1
            if n % 2 == 1:
                result *= current_product
            
            # Square the base for the next iteration (equivalent to moving to the next bit)
            current_product *= current_product
            
            # Divide n by 2 (equivalent to right shifting bits)
            n //= 2
            
        return result
        