class RandomizedCollection:
    def __init__(self):
        self.vals = []  # Stores the values
        # Maps value to a set of indices in self.vals
        self.idx_map = defaultdict(set)

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. 
        Returns true if the collection did not already contain the specified element.
        """
        self.vals.append(val)
        # The index of the newly added value is the last index
        self.idx_map[val].add(len(self.vals) - 1)
        
        # Return true if the set size is 1 (element was not present before)
        return len(self.idx_map[val]) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. 
        Returns true if the collection contained the specified element.
        """
        # Check if val exists in the map and the set of indices is not empty
        if val not in self.idx_map or not self.idx_map[val]:
            return False
        
        # Get an arbitrary index of the value to remove
        remove_idx = self.idx_map[val].pop()
        
        # If the set becomes empty, clean up the key to save space
        if not self.idx_map[val]:
            del self.idx_map[val]
        
        # Get the last element in the list
        last_val = self.vals[-1]
        
        # Move the last element to the position of the element to remove
        self.vals[remove_idx] = last_val
        
        # Remove the last element from the list
        self.vals.pop()
        
        # Update the index map for the element that was moved (last_val)
        # We only need to do this if the element we removed was not the last element itself.
        # len(self.vals) is now the size after popping, so the old last index was len(self.vals).
        if remove_idx != len(self.vals):
            self.idx_map[last_val].discard(len(self.vals))
            self.idx_map[last_val].add(remove_idx)
            
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.vals)