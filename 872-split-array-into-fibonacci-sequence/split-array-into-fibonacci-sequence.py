class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        res = []
    
        def backtrack(index):
        # If reached end and valid sequence
            if index == len(num) and len(res) >= 3:
                return True
        
            curr = 0
            for i in range(index, len(num)):
            # ❌ Leading zero check
                if i > index and num[index] == '0':
                    break
            
                curr = curr * 10 + int(num[i])
            
            # ❌ 32-bit overflow
                if curr > 2**31 - 1:
                    break
            
            # ✅ Fibonacci condition
                if len(res) >= 2:
                    if curr < res[-1] + res[-2]:
                        continue
                    elif curr > res[-1] + res[-2]:
                        break
            
            # Choose
                res.append(curr)
            
            # Recurse
                if backtrack(i + 1):
                    return True
            
            # Backtrack
                res.pop()
        
            return False
    
        backtrack(0)
        return res
        