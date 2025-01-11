# concept is same as Kunal kushwaha video
class Node:

    def __init__(self,value):

        self.data  =  value

        self.next = None

class LL :

    def __init__(self):

        self.head = None
        self.tail = None

    def appendFirst(self , value):
        node = Node(value)

        if self.head is None:

            node.next = self.head

            self.head = node

            self.tail = self.head

            return

        node.next = self.head

        self.head = node

        return

# display the DATA values of each node from head to tail
    def display(self):
        itr = self.head

        while itr is not None :
            print(itr.data,end="->")
            itr = itr.next


ll  = LL()

ll.appendFirst(10)
ll.appendFirst(11)
ll.appendFirst(12)

ll.display()
