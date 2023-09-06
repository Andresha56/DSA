



class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None
    # ---------- Traversing a linked----------

    def printLL(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, " ", " => ", " ", end="")
                current = current.ref

    # ------add element--at --begin---

    def add_element_at_begin(self, data):

        node = Node(data)
        node.ref = self.head
        self.head = node

    # -------at element--at--end---------

    def add_element_at_end(self, data):
        node = Node(data)
        if (self.head == None):
            self.head = node
        else:
            current = self.head
            while (current.ref is not None):
                current = current.ref
            current.ref = node

    # ---------insert before---the --given ---node----------

    def insert_node_before(self, data, x):
        node = Node(data)
        if (x == self.head.data):
            print("match")
            node.ref = self.head
            self.head = node

        else:
            current = self.head
            while current.ref is not None:
                if current.ref.data == x:
                   break
                current = current.ref
            if (current.ref is None):
                print("Node not found")
            else:
                node.ref = current.ref
                current.ref = node


