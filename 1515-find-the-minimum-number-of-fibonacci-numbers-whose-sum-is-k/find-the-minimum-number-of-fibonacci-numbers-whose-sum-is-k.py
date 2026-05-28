class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]

        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])

        count = 0
        i = len(fib) - 1

        # Greedy selection
        while k > 0:

            if fib[i] <= k:
                k -= fib[i]
                count += 1
            else:
                i -= 1

        return count
        