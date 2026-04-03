class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_subsequence(s: str, t: str) -> bool:
            """
            Checks if string s is a subsequence of string t.
            """
            it = iter(t)
            # This consumes the iterator 'it' until all characters in s are found.
            # If a character in s is not found in the remaining part of t, it returns False.
            return all(char in it for char in s)

        # Sort strings by length in descending order to prioritize longer candidates
        strs.sort(key=len, reverse=True)

        for i, candidate in enumerate(strs):
            is_uncommon = True
            for j, other in enumerate(strs):
                if i == j:
                    continue
                
                # If the candidate is a subsequence of any other string, it is not an uncommon subsequence.
                # By definition, it must be a subsequence of exactly one string (itself).
                if is_subsequence(candidate, other):
                    is_uncommon = False
                    break
            
            # If the loop completes without finding a match, the candidate is valid
            if is_uncommon:
                return len(candidate)
        
        # No uncommon subsequence found
        return -1
        