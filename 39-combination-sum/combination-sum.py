class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, target, current):
            # Target reached
            if target == 0:
                result.append(current.copy())
                return

            # Try candidates
            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > target:
                    continue

                current.append(num)

                # i, not i + 1
                # because the same number can be reused
                backtrack(i, target - num, current)

                # Backtrack
                current.pop()

        backtrack(0, target, [])
        return result
        