# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        curr=head
        top=head
        while top is not None and top.next is not None:
            curr=curr.next
            top=top.next.next
        return curr