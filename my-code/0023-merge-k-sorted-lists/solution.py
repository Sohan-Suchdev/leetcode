# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None

        while len(lists)>1:
            merged = []

            i = 0
            while i < len(lists):
                if i == len(lists)-1:
                    merged.append(lists[i])
                    i+=1
                else:
                    merged.append(self.merge2Lists(lists[i], lists[i+1]))
                    i+=2
            
            lists = merged
        
        return lists[0]
        
    
    def merge2Lists(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next 
            
        if l1 is not None:
            curr.next = l1
        elif l2 is not None:
            curr.next = l2
            
        return dummy.next

        
        
