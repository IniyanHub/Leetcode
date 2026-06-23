class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alice = 0
        bob = 0

        count = 1

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                count += 1
            else:
                if colors[i - 1] == 'A':
                    alice += max(0, count - 2)
                else:
                    bob += max(0, count - 2)
                count = 1

        # Process last group
        if colors[-1] == 'A':
            alice += max(0, count - 2)
        else:
            bob += max(0, count - 2)

        return alice > bob
        