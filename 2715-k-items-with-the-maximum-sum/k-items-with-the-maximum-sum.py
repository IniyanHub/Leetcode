class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        
        # Take all 1s
        sum_val = numOnes
        k -= numOnes
        
        # Use 0s next
        if k <= numZeros:
            return sum_val
        
        # Remaining must be -1s
        k -= numZeros
        
        return sum_val - k
        