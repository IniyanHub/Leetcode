class Solution:
    def fractionAddition(self, expression: str) -> str:
        i = 0
        n = len(expression)
    
        num = 0   # numerator
        den = 1   # denominator
    
        while i < n:
        # sign
            sign = 1
            if expression[i] == '+' or expression[i] == '-':
                if expression[i] == '-':
                    sign = -1
                i += 1
        
        # numerator
            curr_num = 0
            while i < n and expression[i].isdigit():
                curr_num = curr_num * 10 + int(expression[i])
                i += 1
        
            curr_num *= sign
        
            i += 1  # skip '/'
        
        # denominator
            curr_den = 0
            while i < n and expression[i].isdigit():
                curr_den = curr_den * 10 + int(expression[i])
                i += 1
        
        # add fractions: num/den + curr_num/curr_den
            num = num * curr_den + curr_num * den
            den = den * curr_den
        
        # reduce fraction
            g = gcd(abs(num), den)
            num //= g
            den //= g
    
        return f"{num}/{den}"
        