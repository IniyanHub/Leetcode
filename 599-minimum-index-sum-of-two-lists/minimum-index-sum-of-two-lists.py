class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {val: i for i, val in enumerate(list1)}
    
        min_sum = float('inf')
        result = []
    
        for j, val in enumerate(list2):
            if val in index_map:
                i = index_map[val]
                s = i + j
            
                if s < min_sum:
                    min_sum = s
                    result = [val]
                elif s == min_sum:
                    result.append(val)
    
        return result
        