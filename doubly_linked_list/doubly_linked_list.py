"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        if node is not None: 
            self.length = 1 
            self.head = node
            self.tail = node
        else: 
            self.length = 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
        else:
            self.head = new_node
            self.tail = new_node

        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head.next is not None:
            val = self.head.value
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return val
        elif self.head is None:
            return
        else:
            val = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.tail is not None:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.tail.prev is not None:
            val = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return val
        elif self.head is None:
            return
        else:
            val = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node.prev is None:
            return
        elif node.next is None:
            node.prev.next = None
            self.tail = node.prev
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
            
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node.next is None:
            return
        elif node.prev is None:
            node.next.prev = None
            self.head = node.next
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.tail is node:
            return self.remove_from_tail()
            
        elif self.head is node:
            return self.remove_from_head()
        
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            self.length -= 1
            return node.value


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return
        else:
            current_max = self.head.value
            current_node = self.head
            while current_node is not None:
                if current_node.value > current_max:
                    current_max = current_node.value
                current_node = current_node.next
            return current_max

        