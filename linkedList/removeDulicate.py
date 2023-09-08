
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

    def insert_node_end(self,data,x):
        node=Node(data)
        if self.head is None:
            print("Linked Listis empty")
        else:
            current=self.head
            while current.ref is not None:
                if current.data is x:
                    break
                current=current.ref
            if current.ref is None:
                print("Node not found")
            else:
                node.ref=current.ref
                current.ref=node
                
    # ------------reverse--a--linked---list-----------
    def reverse_Linked_list(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.ref
            current.ref = prev
            prev = current
            current = next_node

        self.head = prev
    # -----remove---buplicate--sorted--link-----
    def remove_duplicates(self):
        if self.head ==None:
            print("Linked list is empty!")
        current=self.head
        while current is not None:
            if current.data==current.ref.data:
                current.ref =current.ref.ref
                print(current.data)
            current=current.ref

            
