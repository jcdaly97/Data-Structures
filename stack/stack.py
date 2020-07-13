from singly_linked_list import Node
from singly_linked_list import LinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        #self.data = []
        self.data = LinkedList()

    def __len__(self):
        #return len(self.data)
        return self.size

    def push(self, value):
        #self.data.append(value)
        self.data.insert_head(value)
        self.size+=1
    def pop(self):
        #if len(self.data) is 0:
        #    return None
        #else:
        #    val = self.data[len(self.data) - 1]
        #    self.data.pop(len(self.data) - 1)
        #    return val
        if self.data.head is None:
            return None

        else:
            val = self.data.head.get_data()
            self.data.remove_head()
            self.size-=1
            return val
