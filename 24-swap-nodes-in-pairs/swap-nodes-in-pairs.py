# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        # 'prev' will point to the node before the pair we are about to swap.
        prev = dummy
        
        # Loop as long as there are at least two nodes to swap.
        while prev.next and prev.next.next:
            # Identify the two nodes to be swapped.
            first = prev.next
            second = prev.next.next
            
            # Perform the swap by adjusting the pointers.
            # 1. The node before the pair (prev) should point to the second node.
            prev.next = second
            # 2. The first node should point to the node after the second node.
            first.next = second.next
            # 3. The second node should point to the first node.
            second.next = first
            
            # Move 'prev' to the end of the swapped pair to prepare for the next iteration.
            prev = first
            
        # The new head of the list is the node after the dummy node.
        return dummy.next