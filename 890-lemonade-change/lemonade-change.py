class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        
        for bill in bills:
            
            # Customer pays with $5
            if bill == 5:
                five += 1
            
            # Customer pays with $10
            elif bill == 10:
                
                if five == 0:
                    return False
                
                five -= 1
                ten += 1
            
            # Customer pays with $20
            else:
                
                # Prefer 10 + 5
                if ten > 0 and five > 0:
                    ten -= 1
                    five -= 1
                
                # Otherwise use three 5s
                elif five >= 3:
                    five -= 3
                
                else:
                    return False
        
        return True
        