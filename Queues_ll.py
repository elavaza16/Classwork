class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None #points to first node in the queue
        self.rear = None #points to the last node in the queue
        self.size = 0 #tracks the number of elements in the queue

    def __len__(self):
        return self.size # returns number of elements in the queue

    def __repr__(self): # returns a string representation of the items in the queue
        items = [] # empty list
        current_item = self.front # starts from the front

        while current_item is not None: # continues until we've moved past the last node
            items.append(str(current_item.value)) # converts value of current node to string
            current_item = current_item.next # moves pointer to the next node
        return ','.join(items) # joins all strings in the list to one string separated by ','

    def enqueue(self,value): #adds an item at the back
        new_node = Node(value)

        # Check if queue is empty
        if self.rear is None:
            self.front = self.rear = new_node # as the queue has only one element

        else:
            self.rear.next = new_node # update pointer
            self.rear = new_node # update the node
            self.size += 1 #increments count of elements in the queue

    def dequeue(self): # removes item from the front
        if self.front is None: #checks if queue is initially empty
            raise IndexError('Queue is empty!')

        dequeue_value = self.front.value #saves value of front node
        self.front = self.front.next #moves pointer to the next node in queue

        if self.front is None: #checks if queue has become empty after removing an element
            self.rear = None

        self.size -= 1
        return dequeue_value


    def peek(self):
        #check if queue is empty
        if self.front is None:
            raise IndexError('Queue is empty!')
        return self.front.value #returns value of front node


    def is_empty(self):
        return self.front is None #Returns true or false


if __name__=='__main__':
    q = Queue()

    q.enqueue(11)
    q.enqueue(22)
    q.enqueue(33)
    q.enqueue(44)
    q.enqueue(55)
    q.enqueue(66)

    print(q)
    print(len(q))

    print(q.dequeue())
    print(q.dequeue())
    print(q)
    print(len(q))
