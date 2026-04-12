class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
        # Step 1: pack words
            line_len = len(words[i])
            j = i + 1

            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = j - i
            total_chars = sum(len(word) for word in line_words)
            spaces = maxWidth - total_chars

        # Step 2: format line
            if j == n or num_words == 1:
            # left-justified
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
            else:
                gaps = num_words - 1
                even_space = spaces // gaps
                extra_space = spaces % gaps

                line = ""
                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (even_space + (1 if k < extra_space else 0))
                line += line_words[-1]

            res.append(line)
            i = j

        return res
        