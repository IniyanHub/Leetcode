class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1

        queue = deque([("0000", 0)])
        visited = set(["0000"])

        def neighbors(code):
            res = []
            for i in range(4):
                digit = int(code[i])
            
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_code = code[:i] + str(new_digit) + code[i+1:]
                    res.append(new_code)
            return res

        while queue:
            code, steps = queue.popleft()

            if code == target:
                return steps

            for nei in neighbors(code):
                if nei not in visited and nei not in dead:
                    visited.add(nei)
                    queue.append((nei, steps + 1))

        return -1
        