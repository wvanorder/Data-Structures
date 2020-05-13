"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if not self.value:
            self.value = value
        else:
            if self.value == value:
                link = self.right
                self.right = BSTNode(value)
                self.right.right = link
            if self.value < value:
                if self.right is None:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value)
            else:
                if self.left is None:
                    self.left = BSTNode(value)
                else:
                    self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        #criteria for returning False: we know we need to go in one direction
        # but there is nothing in that direction
        if target == self.value:
            return True
        if not self.left and not self.right:
            return False
        if target < self.value:
            #if there is no left child
            if not self.left:
                return False
            #go left
            return self.left.contains(target)
        else:
            #if there is no left child
            if not self.right:
                return False
            # go right
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None and self.left is None:
            return self.value
        elif self.right is not None:
            return self.right.get_max()
        else:
            return self.left.get_max()
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        else:
            self.in_order_print(node.left) 
            print(node.value)
            self.in_order_print(node.right)
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return
        queue = []
        queue.append(node)

        while(len(queue) > 0):
            print(queue[0].value)
            newParent = queue.pop(0)

            if node.left is not None:
                queue.append(newParent.left)
            if node.right is not None:
                queue.append(newParent.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
       pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is None:
            return
        print(node.value)
        if node.left is None and node.right is None:
            return
        if node.left is not None:
            return self.left.pre_order_dft(node.left)
        if node.right is not None:
            return self.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is None:
            return
        if node.left is not None:
            return self.left.post_order_dft(node.left)
