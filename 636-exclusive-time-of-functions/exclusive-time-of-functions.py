class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        
        prev_time = 0
        
        for log in logs:
            parts = log.split(':')
            fid = int(parts[0])
            typ = parts[1]
            time = int(parts[2])
            
            if typ == 'start':
                # If the stack is not empty, the previous function on the stack
                # has been running from prev_time to time - 1.
                if stack:
                    res[stack[-1]] += time - prev_time
                stack.append(fid)
                prev_time = time
            else:
                # The function ending is at the top of the stack.
                # It runs from prev_time to time (inclusive).
                res[stack[-1]] += time - prev_time + 1
                stack.pop()
                # The next event starts at time + 1
                prev_time = time + 1
                
        return res
        