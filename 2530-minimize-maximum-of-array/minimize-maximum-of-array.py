class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix_sum = 0
        answer = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            # Ceiling of prefix_sum / (i + 1)
            avg = (prefix_sum + i) // (i + 1)

            answer = max(answer, avg)

        return answer
        