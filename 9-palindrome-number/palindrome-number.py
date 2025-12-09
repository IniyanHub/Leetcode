class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        # Reverse half of the number
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        # For an even number of digits, x == reverted_number.
        # For an odd number of digits, x == reverted_number // 10 (to discard the middle digit).
        return x == reverted_number or x == reverted_number // 10
        