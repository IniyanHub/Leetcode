class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(word, pattern):
            i = 0

            for ch in word:
                # Match current pattern character
                if i < len(pattern) and ch == pattern[i]:
                    i += 1

                # Extra uppercase letter not allowed
                elif ch.isupper():
                    return False

            # All pattern characters must be matched
            return i == len(pattern)

        return [match(q, pattern) for q in queries]
        