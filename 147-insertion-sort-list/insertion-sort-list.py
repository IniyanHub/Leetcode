# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(-1)
        
        # 'current' will iterate through the original unsorted list.
        current = head
        
        while current:
            # Before we rewire 'current' to insert it into the sorted list,
            # we must store a reference to the next node in the unsorted list.
            # This allows us to continue our iteration after the insertion.
            next_to_process = current.next
            
            # Find the correct position to insert 'current' in the sorted list.
            # 'sorted_pointer' will be the node after which 'current' should be inserted.
            # We start the search from the dummy head each time.
            sorted_pointer = dummy_head
            while sorted_pointer.next and sorted_pointer.next.val < current.val:
                sorted_pointer = sorted_pointer.next
                
            # Insert 'current' into the sorted list.
            # This involves two steps:
            # 1. Point the new node ('current') to the rest of the sorted list.
            # 2. Point the previous node ('sorted_pointer') to our new node.
            current.next = sorted_pointer.next
            sorted_pointer.next = current
            
            # Move to the next node in the original unsorted list.
            current = next_to_process
            
        # The head of the sorted list is the node after the dummy node.
        return dummy_head.next
        