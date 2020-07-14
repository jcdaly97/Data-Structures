class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def next_get(self):
        return self.next_node

    def next_set(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_head(self, data):
        new = Node(data)
        if self.head is None and self.tail is None:
            self.head = new
            self.tail = new
        else:
            new.next_set(self.head)
            self.head = new
    
    def insert_tail(self, data):
        new = Node(data)
        if self.head is None and self.tail is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next_set(new)
            self.tail = new

    def remove_tail(self):
        if self.head is None and self.tail is None:
            return
        else:
            current = self.head
            while current.next_get is not self.tail:
                current = current.next_get
            val = self.tail.data
            self.tail = None
            self.tail = current
            return val
    
    def remove_head(self):
        if self.head is None and self.tail is None:
            return
        else:
            val = self.head.data
            self.head = self.head.next_get()
            return val

    def get_length(self):
        if self.head is None and self.tail is None:
            return None
        else:
            length = 0
            current = self.head
            while current is not None:
                length += 1
                current = current.next_get()
            return length
                
                  
