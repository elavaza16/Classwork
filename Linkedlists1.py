class linkedlistNode: #every data element exists independently
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode


node1 = linkedlistNode("1")
node2 = linkedlistNode("2")
node3 = linkedlistNode("3")
node4 = linkedlistNode("4")
node5 = linkedlistNode("5")
node6 = linkedlistNode("6")
node7 = linkedlistNode("7")
node8 = linkedlistNode("8")
node9 = linkedlistNode("9")
node10 = linkedlistNode("10")

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4   #pointer for node4 would be None
node4.nextNode = node5
node5.nextNode = node6
node6.nextNode = node7
node7.nextNode = node8
node8.nextNode = node9
node9.nextNode = node10
node10.nextNode = None

currentNode = node1 #setting the first chain link as the head of our link
while True:
    print(currentNode.value, ">>>", end=' ')

    if currentNode.nextNode is None:   #if we are at the end of the list or the list has only one element
        print("None")
        break
    currentNode = currentNode.nextNode #increment from current node till the last one


# if name == '__main__':