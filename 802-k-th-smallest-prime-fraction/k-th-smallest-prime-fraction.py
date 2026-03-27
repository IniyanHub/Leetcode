class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0.0, 1.0
        
        # Binary search to find the value of the k-th smallest fraction
        while right - left > 1e-9:
            mid = (left + right) / 2
            count = 0
            p = 0
            
            # Count how many fractions are <= mid using two pointers
            for j in range(1, n):
                # Expand p while the fraction arr[p]/arr[j] <= mid
                # Since arr is sorted, arr[p] <= mid * arr[j]
                while p < j and arr[p] <= mid * arr[j]:
                    p += 1
                count += p
            
            if count < k:
                left = mid
            else:
                right = mid
        
        # Find the pair with the fraction value closest to 'right' (or 'left')
        # Since 'right' converged to the k-th smallest value.
        res = [0, 1]
        min_diff = float('inf')
        
        for i in range(n):
            for j in range(i + 1, n):
                val = arr[i] / arr[j]
                diff = abs(val - right)
                if diff < min_diff:
                    min_diff = diff
                    res = [arr[i], arr[j]]
                    
        return res
        