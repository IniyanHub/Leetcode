class Solution:
    def __init__(self, nums: List[int]):
        """
        Initializes the object with the integer array nums.
        We store the original array to reset to it later,
        and a copy of the array to perform operations on.
        """
        self.original = nums[:]
        self.array = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.original[:]
        return self.array

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        Uses the Fisher-Yates algorithm for O(n) time complexity.
        """
        # Iterate from the last element down to the second element
        for i in range(len(self.array) - 1, 0, -1):
            # Pick a random index from 0 to i
            j = random.randint(0, i)
            
            # Swap the current element with the randomly picked element
            self.array[i], self.array[j] = self.array[j], self.array[i]
            
        return self.array