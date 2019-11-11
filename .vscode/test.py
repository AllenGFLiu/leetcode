from typing import Optional


class Node:
    
    def __init__(self, value: int):
        self.val = value
        self.next = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.head = Node(None)
        self.tail = self.head
        self.count = 0
        self.capacity = k
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.count += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.count == self.capacity:
            return False
        
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.count += 1
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        self.head = self.head.next
        self.count -= 1
        return True
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.count == 0:
            return False
        node = self.head
        while node:
            if node.next == self.tail:
                node.next = None
                self.tail = node
                self.count -= 1
                return True
            node = node.next
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.count:
            return self.head.val
        else:
            return -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.count:
            return self.tail.val
        else:
            return -1
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if self.count:
            return False
        else:
            return True
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if self.count == self.capacity:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyCircularDeque(3)
    param_1 = obj.insertFront(value)
    param_2 = obj.insertLast(value)
    param_3 = obj.deleteFront()
    param_4 = obj.deleteLast()
    param_5 = obj.getFront()
    param_6 = obj.getRear()
    param_7 = obj.isEmpty()
    param_8 = obj.isFull()