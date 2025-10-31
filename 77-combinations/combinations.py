class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res: List[List[int]] = []

        def backtrack(start: int, path: List[int]) -> None:
        # If the path already has k numbers, store a copy.
            if len(path) == k:
                res.append(path.copy())
                return

        # Number of positions still needed.
            need = k - len(path)

        # The largest possible first element we can pick now.
        # We must leave enough numbers after it: i + need - 1 ≤ n
        # → i ≤ n - need + 1
            for i in range(start, n - need + 2):   # inclusive upper bound
                path.append(i)          # choose i
                backtrack(i + 1, path)  # next element must be larger
                path.pop()              # undo choice (backtrack)

    # Edge cases
        if k == 0:
            return [[]]          # the empty combination
        if k > n:
            return []            # impossible to pick more than n numbers

        backtrack(1, [])
        return res
        