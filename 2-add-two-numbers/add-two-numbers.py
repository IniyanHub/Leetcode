# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_head = ListNode(0)
        
        # 'current' will point to the last node in the result list as we build it.
        current = dummy_head
        
        # 'carry' will store the carry-over value for each digit addition.
        carry = 0
        
        # Loop until we have processed all digits from both lists and there is no carry left.
        while l1 or l2 or carry:
            # Get the value from the current node of l1. If l1 is exhausted, use 0.
            val1 = l1.val if l1 else 0
            
            # Get the value from the current node of l2. If l2 is exhausted, use 0.
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum for the current digit position.
            total_sum = val1 + val2 + carry
            
            # The new digit is the remainder of the sum divided by 10.
            digit = total_sum % 10
            
            # The new carry is the integer division of the sum by 10.
            carry = total_sum // 10
            
            # Create a new node with the calculated digit.
            new_node = ListNode(digit)
            
            # Append the new node to the result list.
            current.next = new_node
            
            # Move the 'current' pointer to the newly added node.
            current = current.next
            
            # Move to the next nodes in the input lists if they exist.
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # The actual result list starts after the dummy head.
        return dummy_head.next

        