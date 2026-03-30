class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if startGene == endGene:
            return 0

    # Convert the bank into a set for O(1) look‑ups.
        bank_set = set(bank)

    # If the end gene is not in the bank, it can never be reached.
        if endGene not in bank_set:
            return -1

    # BFS initialization.
        queue = deque()
        queue.append((startGene, 0))          # (current gene, number of mutations so far)
        visited = {startGene}

    # The four possible nucleotides.
        nucleotides = {'A', 'C', 'G', 'T'}

        while queue:
            gene, steps = queue.popleft()

        # Generate all possible one‑mutation neighbors.
            for i in range(8):
                for ch in nucleotides:
                    if ch == gene[i]:
                        continue
                # Create the mutated gene.
                    neighbor = gene[:i] + ch + gene[i+1:]

                # If we reached the target, return steps+1.
                    if neighbor == endGene:
                        return steps + 1

                # Only proceed if the neighbor is a valid bank gene and not visited.
                    if neighbor in bank_set and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, steps + 1))

    # Target not reachable.
        return -1

        