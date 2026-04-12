class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
    
        seen_digit = False
        seen_dot = False
        seen_exp = False
        digit_after_exp = True
    
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
                if seen_exp:
                    digit_after_exp = True
        
            elif char in ['+', '-']:
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
        
            elif char == '.':
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
        
            elif char in ['e', 'E']:
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                digit_after_exp = False
        
            else:
                return False
    
        return seen_digit and digit_after_exp
        