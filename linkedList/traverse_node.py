
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
