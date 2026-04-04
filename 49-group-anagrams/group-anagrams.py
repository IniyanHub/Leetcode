class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the characters of the string to use as the key.
            # "eat", "tea", "ate" all become "aet".
            # sorted(s) returns a list of characters, so we join them back into a string.
            sorted_key = "".join(sorted(s))
            
            # Append the original string to the list corresponding to its sorted key
            anagram_map[sorted_key].append(s)
        
        # Return the values of the dictionary, which are the grouped anagrams
        return list(anagram_map.values())
        