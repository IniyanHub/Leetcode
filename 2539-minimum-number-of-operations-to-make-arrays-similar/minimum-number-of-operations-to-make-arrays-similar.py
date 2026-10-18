class Solution:
    def makeSimilar(self, nums: list[int], target: list[int]) -> int:
        nums_even = sorted(x for x in nums if x % 2 == 0)
        nums_odd = sorted(x for x in nums if x % 2 == 1)

        target_even = sorted(x for x in target if x % 2 == 0)
        target_odd = sorted(x for x in target if x % 2 == 1)

        surplus = 0

        for a, b in zip(nums_even, target_even):
            if a > b:
                surplus += a - b

        for a, b in zip(nums_odd, target_odd):
            if a > b:
                surplus += a - b

        return surplus // 2
        