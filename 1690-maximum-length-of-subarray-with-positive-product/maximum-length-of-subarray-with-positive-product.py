class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        positive = 0
        negative = 0
        answer = 0

        for num in nums:

            if num == 0:
                # Zero breaks the subarray
                positive = 0
                negative = 0

            elif num > 0:
                # Positive keeps the sign unchanged
                positive += 1

                if negative > 0:
                    negative += 1

            else:
                # Negative changes positive <-> negative
                old_positive = positive

                if negative > 0:
                    positive = negative + 1
                else:
                    positive = 0

                negative = old_positive + 1

            answer = max(answer, positive)

        return answer
        