from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
         return "".join(char * freq for char, freq in Counter(s).most_common())