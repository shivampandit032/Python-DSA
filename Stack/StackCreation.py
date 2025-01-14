class CustomStack:

    def __init__(self):

        self.stack = [0]*10

        self.size = 0

        self.ptr = -1

    def  push(self, value):

        if self.isFull() :

            print("Stack is Full")

            return

        self.ptr += 1

        self.stack[self.ptr] = value

        self.size += 1

        return

    def pop(self) -> int :

        if self.isEmpty():

            print("Stack is Empty")

            return  -1

        num = self.stack[self.ptr]

        self.ptr -= 1

        return num

    def isEmpty(self):
        if self.ptr == -1 :

            return True

        else:

            return False

    def isFull(self):

        if self.ptr == len(self.stack)-1:

            return True

        return False

stack = CustomStack()

for i in range(0,10):

    stack.push(i)

for i in range(0,10):
    print(stack.pop(),end="->")
