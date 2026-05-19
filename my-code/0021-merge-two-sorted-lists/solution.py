# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        elif list1.val<=list2.val:
            new = self.mergeTwoLists(list1.next,list2)
            list1.next = new
            return list1
        else:
            new = self.mergeTwoLists(list2.next,list1)
            list2.next = new
            return list2
        
