# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        Reverses nodes of the linked list in groups of k.
        """
        # Create a dummy node to serve as the anchor before the head
        # This simplifies handling the head change when the first group is reversed
        dummy = ListNode(0)
        dummy.next = head
        
        # 'prev_group_end' points to the node immediately before the current group
        prev_group_end = dummy
        
        while True:
            # Step 1: Check if there are at least k nodes remaining to reverse
            # We advance 'kth_node' k times from the node after prev_group_end
            kth_node = prev_group_end
            count = 0
            while kth_node and count < k:
                kth_node = kth_node.next
                count += 1
            
            # If we couldn't find k nodes, we've reached the end (or a remainder < k)
            if not kth_node:
                break
            
            # Step 2: Identify boundaries
            # 'next_group_start' is the node immediately following the current group of k nodes
            next_group_start = kth_node.next
            # 'group_tail' is the first node of the current group (it will become the tail after reversal)
            group_tail = prev_group_end.next
            
            # Step 3: Reverse the current group of k nodes
            # Standard iterative reversal
            curr = group_tail
            prev = None
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # After the loop, 'prev' is the new head of the reversed group (originally the kth node)
            new_group_head = prev
            
            # Step 4: Reconnect the reversed group to the main list
            # Link the previous part of the list to the new head of this group
            prev_group_end.next = new_group_head
            # Link the tail of this reversed group to the start of the next group
            group_tail.next = next_group_start
            
            # Step 5: Update pointer for the next iteration
            # The 'prev_group_end' for the next iteration is the tail of the current group
            prev_group_end = group_tail
            
        return dummy.next

        