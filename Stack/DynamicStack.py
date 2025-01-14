class CustomStack:

    def __init__(self):

        self.stack = [0]*10

        self.size = 0

        self.ptr = -1

    def push(self,value):

        if self.isFull():

            self.increaseSize(value)
            pass

        self.ptr += 1

        self.stack[self.ptr] = value
        self.size += 1

        return

    def pop(self):

        if self.isEmpty():

            print("Stack is Empty !")

            return -1

        num = self.stack[self.ptr]

        self.ptr -= 1

        return num

    def isFull(self):

        if self.ptr == len(self.stack)-1 :

            return True

        return  False

    def isEmpty(self):

        if self.ptr == -1:

            return True

        return False

    def increaseSize(self,value):

        n = len(self.stack)

        copy_stack = [0]*(2*n)

        for i in range(0 , len(self.stack)):

            copy_stack[i] = self.stack[i]

        self.stack = copy_stack

        self.ptr += 1

        self.stack[self.ptr] = value

        return



stack = CustomStack()

for i in range(0,202):

    stack.push(i)


for i in range(0 , len(stack.stack)):

    print(stack.stack[i],end=" -> ")

