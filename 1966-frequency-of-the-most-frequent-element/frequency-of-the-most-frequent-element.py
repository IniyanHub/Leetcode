class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left = 0
        total = 0
        answer = 0

        for right in range(len(nums)):

            total += nums[right]

            # Cost to make all elements equal to nums[right]
            while nums[right] * (right - left + 1) - total > k:

                total -= nums[left]
                left += 1

            answer = max(answer, right - left + 1)

        return answer
        