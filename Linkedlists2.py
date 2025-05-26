class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:  #creating a linked list for us that'll contain all values
    def __init__(self):
        self.head = None
        #self.tail = None


    def insertAtTheBeginning(self, new_data):
        new_node = Node(new_data)   #parameter created (inheritance)
        new_node.next = self.head
        self.head = new_node


    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data, end= ' ')
            temp = temp.next
        print()

    def insertAtTheEnd(self, new_data):
        new_node = Node(new_data)

        #first check if it is empty
        if self.head is None:
            self.head = new_node
            return None
        tail = self.head

        while tail.next:
            tail = tail.next
        tail.next = new_node


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.insertAtTheBeginning("Fox")
    linkedList.insertAtTheBeginning("Brown")
    linkedList.insertAtTheBeginning("Quick")
    linkedList.insertAtTheBeginning("The")


    linkedList.printLinkedList()
    linkedList.insertAtTheEnd("Jumps")
    linkedList.printLinkedList()