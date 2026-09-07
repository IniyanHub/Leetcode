class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        target = list(num)

        # Find the k-th next permutation
        for _ in range(k):
            self.nextPermutation(target)

        # Original string
        original = list(num)

        swaps = 0

        # Convert original into target using adjacent swaps
        for i in range(len(target)):
            j = i

            # Find target[i] in original
            while original[j] != target[i]:
                j += 1

            # Move it left using adjacent swaps
            while j > i:
                original[j], original[j - 1] = original[j - 1], original[j]
                swaps += 1
                j -= 1

        return swaps

    def nextPermutation(self, arr):
        n = len(arr)

        # Step 1: Find the first decreasing position
        i = n - 2

        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        # Step 2: Find the smallest digit greater than arr[i]
        if i >= 0:
            j = n - 1

            while arr[j] <= arr[i]:
                j -= 1

            arr[i], arr[j] = arr[j], arr[i]

        # Step 3: Reverse the suffix
        left = i + 1
        right = n - 1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        