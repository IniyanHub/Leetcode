class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(start, target, current):
            if target == 0:
                result.append(current.copy())
                return

            for i in range(start, len(candidates)):
                # Skip duplicate numbers at the same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # No need to continue
                if candidates[i] > target:
                    break

                current.append(candidates[i])

                # i + 1 because each number can be used only once
                backtrack(i + 1, target - candidates[i], current)

                # Backtrack
                current.pop()

        backtrack(0, target, [])
        return result
        