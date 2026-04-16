class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
    
        valid = set()
        result = ""
    
        for word in words:
            if len(word) == 1 or word[:-1] in valid:
                valid.add(word)
            
                if len(word) > len(result):
                    result = word
                elif len(word) == len(result) and word < result:
                    result = word
                
        return result
        