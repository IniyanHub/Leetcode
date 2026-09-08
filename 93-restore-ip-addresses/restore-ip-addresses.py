class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(index, parts, ip):
            # 4 parts created
            if parts == 4:
                if index == len(s):
                    result.append(".".join(ip))
                return

            # Try 1, 2, or 3 digits
            for length in range(1, 4):
                if index + length > len(s):
                    break

                part = s[index:index + length]

                # Leading zero
                if len(part) > 1 and part[0] == '0':
                    continue

                # Value must be <= 255
                if int(part) > 255:
                    continue

                ip.append(part)
                backtrack(index + length, parts + 1, ip)
                ip.pop()

        backtrack(0, 0, [])
        return result
        