class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)

    # If k is 0, all elements qualify
        if k == 0:
            return n

        arr = sorted(nums)

    # Threshold element
        threshold = arr[n - k]

        count = 0

        for num in nums:
            if num < threshold:
                count += 1

        return count
        