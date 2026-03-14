class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

    # Word lists for numbers under 1000
        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
             "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
            "Seventy", "Eighty", "Ninety"]
    # Scale words for each group of three digits
        thousands = ["", "Thousand", "Million", "Billion"]

        def convert_hundreds(n: int) -> str:
            if n==0:
                return ""
            parts = []
        # Hundreds place
            hundreds = n // 100
            if hundreds:
                parts.append(ones[hundreds] + " Hundred")
        # Tens and ones
            remainder = n % 100
            if remainder:
                if remainder < 10:
                    parts.append(ones[remainder])
                elif remainder < 20:
                    parts.append(teens[remainder - 10])
                else:
                    ten_digit = remainder // 10
                    one_digit = remainder % 10
                    parts.append(tens[ten_digit])
                    if one_digit:
                        parts.append(ones[one_digit])
            return " ".join(parts)

    # Process the number in groups of three digits (right to left)
        groups = []
        scale_index = 0
        while num:
            chunk = num % 1000
            if chunk != 0:
                chunk_words = convert_hundreds(chunk)
                if scale_index > 0:
                    chunk_words += " " + thousands[scale_index]
                groups.append(chunk_words)
            num //= 1000
            scale_index += 1

    # The groups were collected from least significant, so reverse them
        return " ".join(reversed(groups))

        