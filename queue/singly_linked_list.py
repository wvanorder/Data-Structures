class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else: 
            current = self.head 
            while current.get_next() is not None:
                current = current.get_next()
            # we're at the end of the linked list 
            current.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        # what if the list is empty?
        if not self.head:
            return None
        # what if it isn't empty?
        else:
            # we want to return the value at the current head 
            current = self.head
            if not current.get_next():
                value = self.head.get_value()
                self.head = None
                self.tail = None
                return value
            else:
            # remove the value at the head 
            # update self.head
                value = self.head.get_value()
                self.head = self.head.get_next()
                return value

    def contains(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.get_next()
        return False

    def get_max(self):
        if not self.head:
            return None
        else:
            current = self.head
            max = self.head
            while current is not None:
                if current.value > max.value:
                    max = current
                current = current.get_next()
            return max.value