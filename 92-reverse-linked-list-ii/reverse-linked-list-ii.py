# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        
        # 2. Find the node before the sublist to be reversed (predecessor)
        predecessor = dummy
        # Move (left - 1) steps from the dummy node to reach the predecessor
        for _ in range(left - 1):
            predecessor = predecessor.next
        
        # 3. Reverse the sublist
        # `prev` will eventually be the new head of the reversed sublist
        # `current` is the node we are currently processing
        prev = None
        current = predecessor.next
        # We need to reverse (right - left + 1) nodes
        for _ in range(right - left + 1):
            next_node = current.next  # Store the next node
            current.next = prev        # Reverse the pointer
            prev = current             # Move prev forward
            current = next_node        # Move current forward
        
        # 4. Reconnect the reversed sublist back into the main list
        # After the loop:
        # - `predecessor.next` is the original start of the sublist (now the tail)
        # - `prev` is the new head of the reversed sublist
        # - `current` is the node after the original right-th node (the successor)
        
        # Connect the tail of the reversed sublist to the successor
        predecessor.next.next = current
        # Connect the predecessor to the new head of the reversed sublist
        predecessor.next = prev
        
        # 5. Return the new head of the list
        return dummy.next
        