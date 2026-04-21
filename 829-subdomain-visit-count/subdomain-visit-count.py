class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        from collections import defaultdict

        count_map = defaultdict(int)

        for entry in cpdomains:
            count, domain = entry.split()
            count = int(count)

            parts = domain.split('.')

        # Generate subdomains
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                count_map[subdomain] += count

    # Format output
        result = []
        for domain, count in count_map.items():
            result.append(f"{count} {domain}")

        return result
        