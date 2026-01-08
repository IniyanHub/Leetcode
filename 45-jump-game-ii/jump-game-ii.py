class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jumps = 0          # number of jumps taken so far
        cur_end = 0        # farthest index reachable with the current number of jumps
        farthest = 0       # farthest index we can reach from the current window

    # We only need to iterate up to the second last index because once we are at
    # the last index, no further jumps are needed.
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

        # When we reach the boundary of the current jump window,
        # we must take another jump to extend the reach.
            if i == cur_end:
                jumps += 1
                cur_end = farthest

            # Early exit: we can already reach the last index.
                if cur_end >= n - 1:
                    break

        return jumps
        