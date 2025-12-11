class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        # Create a boolean list "is_prime" and initialize all entries to True.
        # A value in is_prime[i] will finally be False if i is Not a prime, else True.
        is_prime = [True] * n
        
        # 0 and 1 are not prime numbers
        is_prime[0] = is_prime[1] = False
        
        # Start with the first prime, 2
        # We only need to check up to the square root of n
        for p in range(2, int(math.sqrt(n)) + 1):
            # If is_prime[p] is still True, then it is a prime
            if is_prime[p]:
                # Mark all multiples of p as not prime.
                # Start from p*p, as smaller multiples have been marked already.
                for multiple in range(p * p, n, p):
                    is_prime[multiple] = False
        
        # The final count is the sum of True values in the list from index 2 onwards.
        # (Or sum the whole list, since 0 and 1 are False).
        return sum(is_prime)
        