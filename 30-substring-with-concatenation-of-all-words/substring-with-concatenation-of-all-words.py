class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s:
            return []
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        if len(s) < total_len:
            return []
        
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        
        result = []
        
        for i in range(word_len):
            left = i
            right = i
            current_count = defaultdict(int)
            count = 0
            
            while right + word_len <= len(s):
                word = s[right:right+word_len]
                right += word_len
                
                if word in word_count:
                    current_count[word] += 1
                    count += 1
                    
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left+word_len]
                        current_count[left_word] -= 1
                        left += word_len
                        count -= 1
                    
                    if count == len(words):
                        result.append(left)
                        left_word = s[left:left+word_len]
                        current_count[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    current_count.clear()
                    left = right
                    count = 0
        
        return result
        