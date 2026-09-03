# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            # Check whether current value has duplicates
            if curr.next and curr.val == curr.next.val:
                duplicate = curr.val

            # Skip ALL nodes having this value
                while curr and curr.val == duplicate:
                    curr = curr.next

                prev.next = curr

            else:
            # Current node is unique
                prev = curr
                curr = curr.next

        return dummy.next
        