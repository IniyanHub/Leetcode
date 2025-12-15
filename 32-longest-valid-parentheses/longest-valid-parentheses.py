class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        left, right = 0, 0
        
        # Left to Right Pass
        for char in s:
            if char == '(':
                left += 1
            else: # char == ')'
                right += 1
            
            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left, right = 0, 0
        
        # Right to Left Pass
        left, right = 0, 0
        for char in reversed(s):
            if char == '(':
                left += 1
            else: # char == ')'
                right += 1
            
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left, right = 0, 0
                
        return max_len
        