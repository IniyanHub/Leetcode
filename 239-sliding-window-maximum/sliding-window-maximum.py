class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices
        result = []

        for i in range(len(nums)):
        # Remove elements out of window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

        # Remove smaller elements from back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

        # Add to result when window is ready
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
        