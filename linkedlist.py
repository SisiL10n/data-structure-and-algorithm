class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:

    def __init__(self):
    # Constructor: initialize the head pointer to null
        self.head = None

    def isEmpty(self):
    # Return True if the linked list is empty, otherwise return False
        return (self.head is None)          
    
    def count(self):
    # Return the size of linked list
        countList = 0
        ptr = self.head

        while ptr is not None:
            countList += 1
            ptr = ptr.next            
        return countList

    def printLL(self):
    # print out all the data in the linked list
        ptr = self.head
        dataList = []

        while ptr is not None:
            dataList.append(ptr.data)
            ptr = ptr.next
        print(dataList)

    def getData(self, index):
    # return the data at the given index
        ptr = self.head

        for i in range(index):
            ptr = ptr.next  
        return ptr.data
    
    def updateNode(self, new_data, index):
    # Given a new data and an index, update the data at the given index
        ptr = self.head

        for i in range(index):
            ptr = ptr.next
        ptr.data = new_data

    def insertAtFront(self, data):
    # Given a data, add a node to the beginning of the linked list
        new_node = Node(data)
        first_node = self.head
        new_node.next = first_node
        self.head = new_node

    def removeFront(self):
    # Remove the first node of the linked list
        self.head = self.head.next

    def insertAtEnd(self, data):
    # Given a data, add a node to the end of the linked list
        ptr = self.head
        new_node = Node
        new_node.data = data

        while ptr is not None:
            ptr = ptr.next
        ptr.next = new_node
        
    def removeEnd(self):
    # Remove the last node of the linked list
        ptr = self.head

        while ptr is not None:
            ptr = ptr.next
        ptr = None    
    
    def insertAtIndex(self, data, index):
    # Given a data and an index, add a node at the index location in the linked list
    # index=0 means the beginning of the linked list and so on
    # Your function should verify that the index is valid. If not, print a message and do nothing
        ptr = self.head

        for i in range(index):
            ptr = ptr.next
            if ptr.data is data:
                print("The index is valid")
            else:
                print("The index is invalid")

    def removeAtIndex(self, index):
    # Remove the node at a given index
        ptr = self.head

        for i in range(index):
            ptr = ptr.next
        ptr = ptr.next
    