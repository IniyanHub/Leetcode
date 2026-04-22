from typing import List

class WordFilter:

    def __init__(self, words: List[str]):
        self.lookup = {}
        
        for index, word in enumerate(words):
            # generate all suffix + '#' + word combinations
            for i in range(len(word) + 1):
                suffix = word[i:]
                combined = suffix + '#' + word
                
                # store all prefixes of this combined string
                for j in range(len(combined)):
                    key = combined[:j + 1]
                    self.lookup[key] = index  # overwrite to keep largest index

    def f(self, pref: str, suff: str) -> int:
        return self.lookup.get(suff + '#' + pref, -1)