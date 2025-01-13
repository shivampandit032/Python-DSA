class Node :

    def __init__(self,value):

        self.value = value

        self.next = None

        self.prev = None

class DLL:

    def __init__(self):

        self.head = None

        self.tail = None
# function to add element at first
    def insertAtFirst(self, value):
        node = Node(value)

        if self.head is None :

            node.next = self.head

            self.head = node

            node.next = None

        else :

            node.next = self.head

            self.head.prev = node

            self.head = node

        if self.tail is None :

            self.tail = self.head

        return

# function to display value of Nodes'
    def display(self):
        temp = self.head
        while temp is not None :
            print(temp.value,end="->")

            temp = temp.next
        print("END")

# function to display head and tail values
    def show(self):

        print(f"The data value in head node is : {self.head.value} and the data value in tail node is : {self.tail.value}")

        return

#function to display Values from Tail to Start
    def displayReverse(self):

        temp = self.head

        while temp.next is not None :

            temp = temp.next

        while temp is not None :

            print(temp.value , end="<-")

            temp = temp.prev

        print("START")

        return


# function to insert at Last
    def insertLast(self,value):

        if self.head is None :

            self.insertAtFirst(value)

            return

        node = Node(value)

        temp = self.head

        while temp.next is not None :

            temp = temp.next

        temp.next = node

        node.prev = temp

        node.next = None

        self.tail = node

        return

# function to insert after  a particular Value

    def insertAfterAValue(self, insert_value , value ):

        temp = self.head

        while temp.value is not insert_value :

            temp = temp.next

        node = Node(value)

        node.next = temp.next

        temp.next.prev = node

        temp.next = node

        node.prev = temp

        return


dll = DLL()

dll.insertAtFirst(10)
dll.insertAtFirst(20)
dll.insertAtFirst(30)

# dll.display()
#
# print()
#
# dll.show()
#
# print("Printing values from end to start ",end=" :")
#
# dll.displayReverse()

dll.insertLast(3)

dll.display()

dll.displayReverse()


dll.insertAfterAValue(20,15)

dll.display()

print()

dll.displayReverse()