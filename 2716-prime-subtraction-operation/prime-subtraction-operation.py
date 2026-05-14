class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        def isPrime(x):
            if x < 2:
                return False
            
            for i in range(2, int(x ** 0.5) + 1):
                if x % i == 0:
                    return False
            
            return True
        
        prev = 0
        
        for i in range(len(nums)):
            
            best = nums[i]
            
            # Try all primes smaller than nums[i]
            for p in range(2, nums[i]):
                
                if isPrime(p):
                    new_val = nums[i] - p
                    
                    # Must remain strictly greater than prev
                    if new_val > prev:
                        best = min(best, new_val)
            
            # If current value cannot be greater than prev
            if best <= prev:
                return False
            
            prev = best
        
        return True
        