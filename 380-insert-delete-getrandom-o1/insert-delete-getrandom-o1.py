class RandomizedSet:
    def __init__(self):
        self.vals = []          # list to store values
        self.idx_map = {}       # value -> index in vals

    def insert(self, val: int) -> bool:
        """Insert val if not present. Return True if inserted, False otherwise."""
        if val in self.idx_map:
            return False
        self.idx_map[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        """Remove val if present. Return True if removed, False otherwise."""
        if val not in self.idx_map:
            return False
        idx = self.idx_map[val]
        last_val = self.vals[-1]
        # move the last element to the position of the element to delete
        self.vals[idx] = last_val
        self.idx_map[last_val] = idx
        # remove the last element
        self.vals.pop()
        del self.idx_map[val]
        return True

    def getRandom(self) -> int:
        """Return a random element from the set. All elements equally likely."""
        return random.choice(self.vals)