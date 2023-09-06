
class Node:
    def __int__(self,data):
        self.data=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def printLL(self):
        if(self.head==None):
            print("LinedList is empty")
        else:
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.ref


student1=LinkedList()
student1.printLL()