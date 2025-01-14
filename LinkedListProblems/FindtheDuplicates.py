class Node :

    def __init__(self,value):

        self.val = value

        self.next = None

class LL:

    def __init__(self):

        self.head = None

    def insertion(self, value):

        node = Node(value)

        if self.head is None :

            node.next = self.head

            self.head = node

            return

        node.next = self.head

        self.head = node

        return
    def display(self):

        temp = self.head

        while temp is not None :

            print(temp.val , end= "->")
            temp = temp.next

        print("END")
        return

class Solution:

    def duplicates(self, head):

        temp = head

        self.f(temp)

        return head

    def f(self,temp):
        if temp.next.next is None :

            if temp.val == temp.next.val:

                temp.next = None

                return
        else :

            if temp.val == temp.next.val:

                temp.next = temp.next.next

                temp = temp.next.next

                return self.f(temp)

            else:
                return self.f(temp.next)

ll = LL()
ll.insertion(10)
ll.insertion(10)
ll.insertion(20)
ll.insertion(30)
ll.insertion(40)
ll.insertion(40)

ll.display()

sol = Solution()

ll.head = sol.duplicates(ll.head)

ll.display()



