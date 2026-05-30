class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        
        s = 0      # left_sum - right_sum
        cnt = 0    # left_q - right_q

        for i in range(n // 2):
            if num[i] == '?':
                cnt += 1
            else:
                s += int(num[i])

        for i in range(n // 2, n):
            if num[i] == '?':
                cnt -= 1
            else:
                s -= int(num[i])

        # Odd number of '?' => Alice always wins
        if cnt % 2:
            return True

        # Bob wins only in this exact balanced case
        return s != -cnt // 2 * 9
        