class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        digits.sort()

        rem1 = []  # digits % 3 == 1
        rem2 = []  # digits % 3 == 2

        total = sum(digits)

        for i, d in enumerate(digits):
            if d % 3 == 1:
                rem1.append(i)
            elif d % 3 == 2:
                rem2.append(i)

        remove = set()
        r = total % 3

        if r == 1:
            if rem1:
                remove.add(rem1[0])
            elif len(rem2) >= 2:
                remove.update([rem2[0], rem2[1]])
            else:
                return ""
        elif r == 2:
            if rem2:
                remove.add(rem2[0])
            elif len(rem1) >= 2:
                remove.update([rem1[0], rem1[1]])
            else:
                return ""

        result = [digits[i] for i in range(len(digits)) if i not in remove]

        if not result:
            return ""

        result.sort(reverse=True)

        if result[0] == 0:
            return "0"

        return "".join(map(str, result))
        