# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        while res and res.next:
            if res.val == res.next.val:
                res.next = res.next.next
            else:
                res = res.next
        return head
        
