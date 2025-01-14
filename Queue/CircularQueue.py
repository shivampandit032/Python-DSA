'''
This Type of Queue use to overcome the Time complexity Limitation of  deletion in Queue , which is O(n) .
So , here time complexity in deletion is : O(1)
'''

class CQueue:

    def __init__(self):

        self.queue = [0]*5

        self.front = 0

        self.end = 0

        self.size = 0

    def isFull(self):

        if self.size == len(self.queue):

            return True

        return False

    def isEmpty(self):

        if self.size == 0 :

            return True

        return False

    def insert(self,value):

        if self.isFull():

            print("Queue is Full !")

            return

        self.queue[self.end]  = value
        self.end += 1
        self.end = self.end % len(self.queue)

        self.size += 1

        return

    def remove(self):
        if self.isEmpty():

            print("Queue is Empty !")

            return  -1

        removed = self.queue[self.front]
        self.front += 1
        self.front = self.front % len(self.queue)
        self.size -= 1
        return removed

circular = CQueue()

for i in range(0 , 5):

    circular.insert(i)

print(circular.remove())

circular.insert(133)

for i in range(0, len(circular.queue)):
    print(circular.remove())

print(circular.remove())