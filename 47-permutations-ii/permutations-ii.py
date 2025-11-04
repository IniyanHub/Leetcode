class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                     # bring equal numbers together
        n = len(nums)
        used = [False] * n
        path: List[int] = []
        res: List[List[int]] = []

        def backtrack():
            if len(path) == n:
                # make a copy because path will be mutated later
                res.append(path.copy())
                return

            for i in range(n):
                if used[i]:
                    continue
                # skip duplicates: if the current number equals the previous
                # one and the previous one hasn't been used in this branch,
                # then using the current one would generate a duplicate permutation.
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # choose nums[i]
                used[i] = True
                path.append(nums[i])
                backtrack()
                # undo the choice (backtrack)
                path.pop()
                used[i] = False

        backtrack()
        return res
        