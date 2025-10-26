class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
        # skip duplicate a
            if i > 0 and nums[i] == nums[i - 1]:
                continue

        # early termination: smallest possible sum too big
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
        # early termination: largest possible sum too small
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            for j in range(i + 1, n - 2):
            # skip duplicate b
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

            # prune with the smallest / largest sums for current i, j
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    cur = nums[i] + nums[j] + nums[left] + nums[right]
                    if cur == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                    # move left & right past duplicates
                        left_val, right_val = nums[left], nums[right]
                        while left < right and nums[left] == left_val:
                            left += 1
                        while left < right and nums[right] == right_val:
                            right -= 1

                    elif cur < target:
                        left += 1
                    else:  # cur > target
                        right -= 1

        return res
        