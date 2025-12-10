class Solution:
    def getPermutation(self, n: int, k: int) -> str:
         # 1. list of available digits
        nums = list(range(1, n + 1))

    # 2. factorials: fact[i] = i!
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

    # 3. convert k to zero‑based index
        k -= 1

    # 4. build the answer
        answer = []
        for i in range(n, 0, -1):
            idx = k // fact[i - 1]          # which digit to pick
            answer.append(str(nums.pop(idx)))
            k %= fact[i - 1]                # remainder for next position

        return ''.join(answer)
        