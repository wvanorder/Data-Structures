"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if self.head:
            self.head.insert_before(value)
            self.head = self.head.prev
            self.length += 1
        else:
            self.__init__(node=ListNode(value))
        
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if not self.head:
            return None
        else:
            self.length -=1
            value = self.head.value
            newHead = self.head.next
            self.delete(self.head)
            self.head = newHead
            if not self.head:
                self.tail = None
            return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if self.tail:
            self.tail.insert_after(value)
            self.tail = self.tail.next
            self.length +=1
        else:
            self.__init__(node=ListNode(value))


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        last = self.head
        if self.length == 0:
            self.head = None
            self.tail = None
            return
        elif self.length == 1:
            removed = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return removed
        else:
            while last.next is not None:
                last = last.next.v

            secondToLast = last.prev
            secondToLast.next = None
            self.tail = secondToLast
            self.length -= 1
            return last

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        newHead = node
        currentHead = self.head
        self.head.insert_before(newHead)
        self.head = self.head.prev.value
        self.head.next = currentHead
        

        
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        newTail = node
        currentTail = self.tail
        self.tail = newTail
        self.tail.next = None
        self.tail.prev = currentTail
        print(self.tail.prev.value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if node.prev and node.next:
            self.length -= 1
            node.delete()
        elif node.next and not node.prev:
            self.length -= 1
            self.head = node.next
            self.head.prev = None
        elif node.prev and not node.next:
            self.length -= 1
            self.tail = node.prev
            self.tail.next = None
        elif not node.prev and not node.next:
            self.length = 0
            node.delete()
            self.head = None
            self.tail = None
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if self.length is None:
            return None
        elif self.length == 1:
            return self.head.value
        else:
            max = self.head.value
            index = self.head
            while index is not None:
                if index.value >= max:
                   max = index.value
                   index = index.next
                else:
                    index = index.next
            return max
