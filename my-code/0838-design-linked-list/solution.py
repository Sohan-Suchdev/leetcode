class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        i = 0
        curr = self.head
        while i < index:
            curr = curr.next
            i += 1
        return curr.val
        
    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        if self.size == 0:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        self.size += 1        

    def addAtTail(self, val: int) -> None:
        new = ListNode(val)
        if self.size == 0:
            self.head = new
            self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new  
        self.size += 1        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size or index < 0:
            return
        elif index == self.size:
            self.addAtTail(val)
        elif index == 0:     
            self.addAtHead(val)
        else:
            new = ListNode(val)
            i = 0
            curr = self.head
            while i < index:
                curr = curr.next
                i += 1
            n = curr.prev
            n.next = new
            new.prev = n
            new.next = curr
            curr.prev = new
            self.size += 1   

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        elif index == 0:
            if self.size == 1: 
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            i = 0
            curr = self.head
            while i < index:
                curr = curr.next
                i += 1
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        self.size -= 1
