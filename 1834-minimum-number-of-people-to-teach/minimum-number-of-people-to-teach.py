class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        lang_sets = [set(lang) for lang in languages]

        # Users who are involved in a friendship
        # where they currently cannot communicate
        need_help = set()

        for u, v in friendships:
            u -= 1
            v -= 1

            # Check if they share a language
            if lang_sets[u].isdisjoint(lang_sets[v]):
                need_help.add(u)
                need_help.add(v)

        answer = float('inf')

        # Try teaching each language
        for lang in range(1, n + 1):
            count = 0

            for user in need_help:
                if lang not in lang_sets[user]:
                    count += 1

            answer = min(answer, count)

        return answer
        