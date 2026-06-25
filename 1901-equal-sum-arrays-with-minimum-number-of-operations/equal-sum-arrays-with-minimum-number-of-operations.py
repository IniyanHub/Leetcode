class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)

        if n1 > 6 * n2 or n2 > 6 * n1:
            return -1

        s1, s2 = sum(nums1), sum(nums2)

        if s1 == s2:
            return 0

        if s1 < s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1

        diff = s1 - s2

        gains = []

        for x in nums1:
            gains.append(x - 1)

        for x in nums2:
            gains.append(6 - x)

        gains.sort(reverse=True)

        ops = 0

        for gain in gains:
            diff -= gain
            ops += 1

            if diff <= 0:
                return ops

        return -1
        