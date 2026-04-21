class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_groups(word):
            groups = []
            i = 0
            while i < len(word):
                j = i
                while j < len(word) and word[j] == word[i]:
                    j += 1
                groups.append((word[i], j - i))
                i = j
            return groups

        s_groups = get_groups(s)
        result = 0

        for word in words:
            w_groups = get_groups(word)

            if len(s_groups) != len(w_groups):
                continue

            valid = True
            for (c1, count_s), (c2, count_w) in zip(s_groups, w_groups):
                if c1 != c2:
                    valid = False
                    break
                if count_s < 3:
                    if count_s != count_w:
                        valid = False
                        break
                else:
                    if count_w > count_s:
                        valid = False
                        break

            if valid:
                result += 1

        return result
        