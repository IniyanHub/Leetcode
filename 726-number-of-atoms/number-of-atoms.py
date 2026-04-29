class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1

            elif formula[i] == ')':
                i += 1
                start = i

                # Parse number after ')'
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[start:i] or 1)

                # Pop and merge
                top = stack.pop()
                for elem, count in top.items():
                    stack[-1][elem] += count * multiplier

            else:
                # Parse element name
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                name = formula[start:i]

                # Parse count
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[start:i] or 1)

                stack[-1][name] += count

        # Final result
        result = stack[-1]

        # Sort and build string
        return ''.join(
            elem + (str(result[elem]) if result[elem] > 1 else '')
            for elem in sorted(result)
        )
        