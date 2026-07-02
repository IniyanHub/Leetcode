class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        num = list(num)
        started = False

        for i in range(len(num)):
            digit = int(num[i])

            if not started:
                if change[digit] > digit:
                    started = True
                    num[i] = str(change[digit])
            else:
                if change[digit] >= digit:
                    num[i] = str(change[digit])
                else:
                    break

        return "".join(num)
        