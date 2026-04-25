class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        from collections import Counter

    # Step 1: Convert to lowercase and extract words
        words = re.findall(r'\w+', paragraph.lower())

    # Step 2: Convert banned list to set
        banned_set = set(banned)

    # Step 3: Count only non-banned words
        count = Counter(word for word in words if word not in banned_set)

    # Step 4: Return the most common word
        return count.most_common(1)[0][0]
        