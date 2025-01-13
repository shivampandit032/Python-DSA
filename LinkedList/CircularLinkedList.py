class Node:

    def __init__(self , value):

        self.value = value

        self.next = None

class CLL:

    def __init__(self):

        self.head = None

        self.tail = None

    def insertFirst(self,value):

        node = Node(value)

        if self.head is None :

            self.head = node
            self.tail = self.head
            return

        node.next = self.head

        self.tail.next = node

        self.head = node

        return

# function to display Values

    def displayForward(self):

        temp = self.head

        while temp.next is not self.head :

            print(temp.value,end="->")

            temp = temp.next

        print(temp.value,end="->")

        print("END")

        return

# function to check if it is circular Linked List or Not
    def check(self):
        print(f"value of head node : {self.head.value}")
        print(f"Value of Tail node : {self.tail.value}")

        if self.tail.next is self.head :
            print("This is Circular Linked List")
        else:
            print("Not a Circular Linked List")

        return

# function to Delete node having a Particular Value

    def deleteAtAParticularValue(self , value):

        if self.head.value is value :
            temp = self.head

            self.tail.next = self.head.next

            self.head = self.head.next

            temp.next = None
            return

        temp = self.head.next
        temp2 = self.head

        while temp.next is not self.head and temp.value is not value :
            temp = temp.next
            temp2 = temp2.next

        if temp.value is value :

            temp2.next = temp.next

            temp.next = None

            return
        if temp is self.tail and temp.value is not value :

            print("No Node having this Value")

            return
cll = CLL()

cll.insertFirst(10)
cll.insertFirst(20)
cll.insertFirst(30)
cll.insertFirst(40)

cll.displayForward()

# print()
#
# cll.check()

cll.deleteAtAParticularValue(10)

cll.displayForward()