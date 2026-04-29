class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        # Find function
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        # Union function
        def union(x, y):
            parent[find(x)] = find(y)

        # Step 1: Initialize
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name

        # Step 2: Union emails
        for account in accounts:
            first_email = account[1]
            for email in account[2:]:
                union(first_email, email)

        # Step 3: Group emails
        from collections import defaultdict
        groups = defaultdict(list)

        for email in parent:
            root = find(email)
            groups[root].append(email)

        # Step 4: Build result
        result = []
        for root, emails in groups.items():
            result.append([email_to_name[root]] + sorted(emails))

        return result
        