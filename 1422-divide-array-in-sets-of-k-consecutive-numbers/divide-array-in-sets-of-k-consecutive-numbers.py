class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        count = Counter(nums)

        for num in sorted(count):

            # if current number still exists
            while count[num] > 0:

                # try making consecutive group
                for i in range(num, num + k):

                    if count[i] == 0:
                        return False

                    count[i] -= 1

        return True
        