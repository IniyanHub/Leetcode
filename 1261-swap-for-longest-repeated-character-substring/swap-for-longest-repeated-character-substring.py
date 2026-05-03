class Solution:
    def maxRepOpt1(self, text: str) -> int:
        count = Counter(text)
        res = 0

        for ch in count:
            left = 0
            diff = 0  # number of non-ch characters in window
        
            for right in range(len(text)):
                if text[right] != ch:
                    diff += 1
            
            # allow only one mismatch
                while diff > 1:
                    if text[left] != ch:
                        diff -= 1
                    left += 1
            
            # window size
                window_len = right - left + 1
            
            # cannot exceed total count of ch
                res = max(res, min(window_len, count[ch]))
    
        return res
        