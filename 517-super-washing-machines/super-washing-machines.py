class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total_dresses = sum(machines)
        n = len(machines)
        
        # If total dresses cannot be evenly distributed
        if total_dresses % n != 0:
            return -1
            
        target = total_dresses // n
        res = 0
        balance = 0
        
        for dresses in machines:
            # 'diff' is the surplus or deficit of the current machine
            diff = dresses - target
            
            # 'balance' is the net number of dresses that must flow 
            # from the left side (indices < i) to the right side (indices >= i)
            balance += diff
            
            # The answer is the maximum of:
            # 1. The flow requirement across the current boundary (abs(balance))
            # 2. The maximum outflow capacity of the current machine (diff)
            #    Note: If diff is negative (deficit), it doesn't constrain time
            #    because we can receive from both neighbors simultaneously.
            res = max(res, abs(balance), diff)
            
        return res