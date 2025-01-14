class Node:

    def __init__(self,value):

        self.value = value

        self.next = None

class LL:

    def __init__(self):

        self.head = None

        self.tail = None

        self.size = 0

    def insertFirst(self,value):

        node = Node(value)

        if self.head is None :

            node.next = self.head

            self.head = node

            self.size += 1

            return

        node.next = self.head
        self.head = node

        self.size += 1

        return

    def insertAtAPosition(self, value , i , j, temp):

        if j > self.size+1 :

            print("Node cann't be create at this Index !!")

            print(f"Only index value till {self.size+1} is Allowed")

            return

        if j == 0 :

            self.insertFirst(value)
            self.size += 1

            return

        if i == j-1 :

            node = Node(value)

            node.next = temp.next

            temp.next = node

            self.size += 1

            return

        self.insertAtAPosition(value , i+1 , j , temp.next)

        return
    def displayForward(self):
        temp = self.head

        while temp is not None:

            print(temp.value , end="->")
            temp = temp.next

        print("End")

        print(f"And the size of the LL is : {self.size}")
        return

ll = LL()

ll.insertFirst(11)
ll.insertFirst(9)
ll.insertFirst(5)
ll.insertFirst(3)

ll.displayForward()

ll.insertAtAPosition(7,0,44 , ll.head)

ll.displayForward()
