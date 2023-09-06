
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None
    # ---------- Traversing a linked----------

    def printLL(self):
        if (self.head == None):
            print("LinedList is empty")
        else:
            while self.head is not None:
                print(self.head.data,   " " , "=>" ,end="")
                self.head = self.head.ref

    # ------add element--at --begin---

    def add_element_at_begin(self, data):
        node = Node(data)
        node.ref = self.head
        self.head = node
