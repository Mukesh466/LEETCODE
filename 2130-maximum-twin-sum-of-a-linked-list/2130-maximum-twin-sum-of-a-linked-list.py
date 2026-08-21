# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        curr=slow
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        head2=prev
        maxi=0
        while head2:
            maxi=max(maxi,head.val+head2.val)
            head=head.next
            head2=head2.next
        return maxi