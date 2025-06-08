class Circulararrayqueue:

    default_capacity = 10 #maximum no. of elements that the queue will hold

    def __init__(self):
        # 1. data - list filled with None values
        # 2. size - how many elements are at a given timestamp
        # 3. front - index of first element
        self._data = [None]*Circulararrayqueue.default_capacity #holds elements of the queue in a circular fashion
        self._size = 0
        self._front = 0 #front index to 0

    def __len__(self): #dunder.method (double underscore)
        return self._size #returns current number of elements in the queue

    def is_empty(self): #returns boolean
        return self._size == 0

    def first(self): #returns element at the front of the queue without removing it
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front] # returns item at the front of the queue

    def dequeue(self): #removes and returns the element at the front of the queue
        if self.is_empty():
            raise Empty('Queue is empty!')
        item_to_dequeue = self._data[self._front] #stores item currently at the front
        self._data[self._front] = None # sets the slot at front to None after removing the item
        self._front = (self._front + 1) % len(self._data)
            # moves front pointer one step forward in a circular fashion
            # % - wraps index around to 0 if it reaches the end of the list
        self._size -= 1
        return item_to_dequeue

    def enqueue(self,element): # adds a new element to the rear(back) of the queue
        if self._size == len(self._data): # checks if queue is full by comparing no. of items to the capacity
            self._resize(2 * len(self._data)) # if full, it doubles the capacity of the queue

        back_of_the_queue = (self._front + self._size) % len(self._data)  # calculates index where the new element should be inserted
            # formula ensures new item wraps around to the start if the end of the list is reached
        self._data[back_of_the_queue] = element #places new element in the calculated position of rear of the queue
        self._size += 1

    def _resize(self, new_capacity): #(private method - indicated by _)
        old_data = self._data # reference to the current queue list
        self._data = [None] * new_capacity # creates new list with slots, all set to none
        current_index = self._front # starts copying from the current front of the old queue

        #Loops over no. of elements in queue currently
        for item in range(self._size):
            self._data[item] = old_data[current_index] #copies from old queue to the new list in order
            current_index = (current_index + 1) % len(old_data) #moves to next element
            self._front = 0 #reset to 0 after all elements are copied

class Empty(Exception):
    def __init__(self, message="Queue is empty"):
        self.message = message
        super().__init__(self.message)

