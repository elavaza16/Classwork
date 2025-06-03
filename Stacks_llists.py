# Stack implementation using linked list is conceptual for large data
# As it only allocates memory when needed, hence reducing on memory wastage



class StackNode:   #Node for linked list
    def _init_(self,value):
        self.value = value
        self.next = None

# Stack implemented with linked lists
class LinkedListStack:
    def _init_(self):
        self.top = None  #as the stack is empty

    def is_empty(self):
        return self.top is None

    def push(self,value): #creating a new node
        new_node = StackNode(value) #create
        new_node.next = self.top #new node pointer -> current top node
        self.top = new_node #top pointer -> new node (as it is the new top of the stack)

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop an empty stack!")

        popped_value = self.top.value
        self.top = self.top.next  #Moving the top pointer to next node down the stack
        return popped_value

    def peek(self):
        if self.is_empty():
            raise Exception("Cannot peek an empty stack!")
        return self.top.value

    def display(self):
        current = self.top
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print("Stack from top to bottom:", "->".join(values))


if __name__=="main_":
        stack_11 = LinkedListStack()
        stack_11.push(5)
        stack_11.push(10)
        stack_11.push(15)

        stack_11.display()

        print("Peek top:", stack_11.peek())

        print("Pop:", stack_11.pop())
        stack_11.display()