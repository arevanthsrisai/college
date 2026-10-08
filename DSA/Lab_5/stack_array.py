class stack():
    def __init__(self,n):
        self.stack = [None]*n
        self.top = -1
        self.n = n
    def push(self,data):
        if self.top < self.n - 1:
            self.top += 1
            self.stack[self.top] = data
        else:
            print("Stack overflow")
    def pop(self):
        if self.top > -1:
            print(self.stack[self.top], " is removed")
            self.stack[self.top] = None
            self.top -= 1
        else:
            print("Stack underflow")
    def display(self):
        if self.top == 1:
            print("empty stack")
        for i in self.stack:
            print(i, end = " ")
        print()
    def peek(self):
        if self.top == 1:
        print("empty stack")
        print(self.stack[self.top])
while True:

    print("\n======================================")
    print("       Stack with array")
    print("======================================")

    print("1. Create Linked List with n elements")
    print("2. push")
    print("3. pop")
    print("4. display")
    print("5. peek")
      
    print("10. Exit")

    print("======================================")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        n = int(input("Enter number of elements: "))
        stack1 = stack(n)
        print(f'Created a stack with {n} elements')

    elif ch == 2:
        data = int(input("Enter data: "))
        stack1.push(data)

    elif ch == 3:
        stack1.pop()

    elif ch == 4:
        stack1.display()

    elif ch == 5:
        stack1.peek()

    elif ch == 10:
        print("Exiting program...")
        break
    else:
        print("invalid choise")

