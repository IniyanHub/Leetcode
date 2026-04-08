class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
    
        result = []
    
    # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            result.append('-')
    
    # Convert to positive
        numerator, denominator = abs(numerator), abs(denominator)
    
    # Integer part
        result.append(str(numerator // denominator))
        remainder = numerator % denominator
    
        if remainder == 0:
            return ''.join(result)
    
        result.append('.')
    
    # Map remainder to index in result
        remainder_map = {}
    
        while remainder != 0:
            if remainder in remainder_map:
                index = remainder_map[remainder]
                result.insert(index, '(')
                result.append(')')
                break
        
            remainder_map[remainder] = len(result)
        
            remainder *= 10
            result.append(str(remainder // denominator))
            remainder %= denominator
    
        return ''.join(result)
        