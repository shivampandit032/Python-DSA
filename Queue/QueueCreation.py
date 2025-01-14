
class Queue:

    def __init__(self):

        self.queue = [0]*10

        self.end = -1

        # function to insert element from "Last " . time complexity : O(1)

    def insert(self,value):

        if self.isFull():

            print("Queue is Full !")

            return

        self.end += 1

        self.queue[self.end] = value

        return

    def isFull(self):

        if self.end== len(self.queue)-1:

            return True

        return False

    def  isEmpty(self):

        if self.end == -1 :

            return True

        return False

    # function to delete from "First" . Time complexity : O(n)
    def delete(self):

        if self.isEmpty():

            print("queue is Empty")

            return -1

        num = self.queue[0]

        for i in range(1 , self.end+1):

            self.queue[i-1] = self.queue[i]

        self.end -= 1

        return num

    def show(self):

        print(f"end value : {self.end}")

queue  = Queue()

for i in range(0 , 10):
    queue.insert(i)


queue.show()
for i in range(0,10):

    print(queue.delete())

print(queue.delete())