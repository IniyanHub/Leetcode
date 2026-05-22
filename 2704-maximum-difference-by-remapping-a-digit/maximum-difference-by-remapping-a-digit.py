class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        
        # Maximum value
        mx = s
        for ch in s:
            if ch != '9':
                mx = s.replace(ch, '9')
                break
        
        # Minimum value
        mn = s
        for ch in s:
            if ch != '0':
                mn = s.replace(ch, '0')
                break
        
        return int(mx) - int(mn)
        