class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        eval_map = dict(zip(evalvars, evalints))

        # Polynomial operations
        def add(A, B):
            res = Counter(A)
            for k, v in B.items():
                res[k] += v
                if res[k] == 0:
                    del res[k]
            return res

        def sub(A, B):
            res = Counter(A)
            for k, v in B.items():
                res[k] -= v
                if res[k] == 0:
                    del res[k]
            return res

        def mul(A, B):
            res = Counter()
            for k1, v1 in A.items():
                for k2, v2 in B.items():
                    new_key = tuple(sorted(k1 + k2))
                    res[new_key] += v1 * v2
                    if res[new_key] == 0:
                        del res[new_key]
            return res

        # Convert token → polynomial
        def make(token):
            if token.isdigit():
                return Counter({(): int(token)})
            elif token in eval_map:
                return Counter({(): eval_map[token]})
            else:
                return Counter({(token,): 1})

        # Operator precedence
        def precedence(op):
            return 2 if op == '*' else 1

        # Parse expression
        tokens = re.findall(r'\w+|[\+\-\*\(\)]', expression)
        i = 0

        def parse():
            nonlocal i
            stack = []
            ops = []

            def apply():
                b = stack.pop()
                a = stack.pop()
                op = ops.pop()
                if op == '+':
                    stack.append(add(a, b))
                elif op == '-':
                    stack.append(sub(a, b))
                else:
                    stack.append(mul(a, b))

            while i < len(tokens):
                token = tokens[i]
                i += 1

                if token == '(':
                    stack.append(parse())

                elif token == ')':
                    break

                elif token in '+-*':
                    while ops and precedence(ops[-1]) >= precedence(token):
                        apply()
                    ops.append(token)

                else:
                    stack.append(make(token))

            while ops:
                apply()

            return stack[0]

        poly = parse()

        # Sorting
        def sort_key(item):
            vars_, coeff = item
            return (-len(vars_), vars_)

        result = []
        for vars_, coeff in sorted(poly.items(), key=sort_key):
            if coeff == 0:
                continue
            if vars_:
                result.append(str(coeff) + "*" + "*".join(vars_))
            else:
                result.append(str(coeff))

        return result
        