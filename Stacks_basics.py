# # Push - Add an element to the top of the stack
# # Pop - Remove the top element from the stack
# # Peek - Look at the top element without removing it
# # isEmpty - Check if the stack has any elements
#
# #Python inbuilt method for stacks - List (supports .append(), push(), pop() methods)
# stack = []
#
# stack.append(10)
# stack.append(20)
# stack.append(30)
#
# print("Stack after pushes:", stack)
#
# #Peek at the top element(the last item in list)
# top_element = stack[-1]
# print("Top element is:", top_element)
#
# #Check if stack is empty
# if len(stack) == 0:
#     print("Stack is empty")
# else:
#     print("Stack is not empty")



#Implementation via a Stack class with all key operations
class SimpleStack:
    def __init__(self):
        self.items = [] #empty list

    def is_empty(self):
        return len(self.items) == 0 #returns true if empty

    def push(self, item):
        self.items.append(item) #add item to the top of the stack

    def pop(self):
        if self.is_empty(): #Check first if stack has elements
            raise Exception("Cannot pop an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise  Exception("Stack is empty")
        return self.items[-1] #(-1) as the size of a list is greater than position by one

    def size(self): #returns the number of all elements in the stack
        return len(self.items)

    def print_stack(self):
        print("Stack from bottom to top:", self.items)
        return

if __name__=="__main__":
    stack1 = SimpleStack()

    stack1.push(1000)
    stack1.push(2000)
    stack1.push(3000)

    stack1.print_stack()
    print("Top element:",stack1.peek())

    print("Popped:",stack1.pop())
    stack1.print_stack()

    print("Is stack empty?", stack1.is_empty())

    stack1.pop()
    stack1.pop()
    print("Is stack empty after popping all?", stack1.is_empty())


#.....