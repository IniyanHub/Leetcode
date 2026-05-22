class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count = Counter(basket1) + Counter(basket2)
        
        # If any fruit appears odd number of times -> impossible
        for freq in count.values():
            if freq % 2:
                return -1
        
        c1 = Counter(basket1)
        c2 = Counter(basket2)
        
        extra1 = []
        extra2 = []
        
        # Find extra fruits in both baskets
        for x in count:
            diff = c1[x] - c2[x]
            
            if diff > 0:
                extra1.extend([x] * (diff // 2))
            elif diff < 0:
                extra2.extend([x] * (-diff // 2))
        
        extra1.sort()
        extra2.sort(reverse=True)
        
        smallest = min(min(basket1), min(basket2))
        
        ans = 0
        
        # Perform optimal swaps
        for a, b in zip(extra1, extra2):
            ans += min(min(a, b), 2 * smallest)
        
        return ans
        