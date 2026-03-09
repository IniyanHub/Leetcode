class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        n = len(senate)
        
        # Populate the queues with the initial indices
        for i, party in enumerate(senate):
            if party == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        # Simulate the rounds
        while radiant and dire:
            # Get the senators at the front of the line
            r_index = radiant.popleft()
            d_index = dire.popleft()
            
            # The senator with the smaller index acts first and bans the other
            if r_index < d_index:
                # Radiant bans Dire. Radiant senator gets to vote in the next round.
                # We add 'n' to its index to ensure it goes to the end of the line.
                radiant.append(r_index + n)
            else:
                # Dire bans Radiant. Dire senator gets to vote in the next round.
                dire.append(d_index + n)
        
        # The party with remaining senators wins
        return "Radiant" if radiant else "Dire"
        