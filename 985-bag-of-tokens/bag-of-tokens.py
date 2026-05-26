class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        left = 0
        right = len(tokens) - 1

        score = 0
        max_score = 0

        while left <= right:

            # Play face-up
            if power >= tokens[left]:

                power -= tokens[left]
                score += 1

                max_score = max(max_score, score)

                left += 1

            # Play face-down
            elif score >= 1:

                power += tokens[right]
                score -= 1

                right -= 1

            else:
                break

        return max_score
        