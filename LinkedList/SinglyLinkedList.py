# concept is same as Kunal kushwaha video
class Node:

    def __init__(self,value):

        self.data  =  value

        self.next = None

class LL :

    def __init__(self):

        self.head = None
        self.tail = None

# Function to insert element at first
    def appendFirst(self , value):
        node = Node(value)

        node.next = self.head
        self.head = node

        if self.tail is  None :
            self.tail = self.head


        return

# display the DATA values of each node from head to tail
    def display(self):
        itr = self.head

        while itr is not None :
            print(itr.data,end="->")
            itr = itr.next
        print("END")

# function to insert element at last
    def insertLast(self,value):
        node = Node(value)
        if self.tail is None :
            self.appendFirst(value)
            return
        self.tail.next = node
        self.tail = node

        return

# function to insert a Node at a particular index of the linked List
    def insertAtPosition(self,value,index):

        if index == 0 :
            self.appendFirst(value)
            return

        node = Node(value)

        itr = self.head
        for i in range(1 , index):
            itr = itr.next

        node.next = itr.next

        itr.next = node

        return

# function for deleting first node

    def deleteFirst(self):

        if self.head is not None and self.head.next is None :

            node = self.head

            self.head = node.next

            node.next = None

            return

        node = self.head

        self.head = node.next

        node.next = None

        return

# function to delete last Node
    def deleteLast(self):

        temp = self.head

        while temp.next != self.tail :

            temp = temp.next

        self.tail = temp

        self.tail.next = None

        return

# function to display head and tail
    def show(self):
        print(f"the head value is : {self.head.data} and tail value is : {self.tail.data}")

#function to Delete at a index
    def deleteAtIndex(self,index):
        if index == 0 :
            self.deleteFirst()
            return

        temp = self.head

        for i in range(1 , index-1):

            temp = temp.next

        temp.next = temp.next.next

        return


ll  = LL()

ll.appendFirst(10)
ll.appendFirst(11)
ll.appendFirst(12)
ll.appendFirst(13)
ll.insertAtPosition(111,3)
ll.display()

print()

ll.show()

# ll.deleteLast()

ll.deleteAtIndex(3)

ll.display()

