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
        new_node = Node(data)

        if ptr is None:
            self.head = new_node
        else:
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = new_node
        
    def removeEnd(self):
    # Remove the last node of the linked list
        ptr = self.head
        pre_ptr = self.head

        if ptr is None:
            print("List is already empty")
        elif ptr.next is None:
            self.head = None
        else:
            while ptr.next is not None:
                pre_ptr = ptr
                ptr = ptr.next
            pre_ptr.next = None
            
              
    
    def insertAtIndex(self, data, index):
    # Given a data and an index, add a node at the index location in the linked list
    # index=0 means the beginning of the linked list and so on
    # Your function should verify that the index is valid. If not, print a message and do nothing
        ptr = self.head
        pre_ptr = self.head
        new_node = Node(data)
        countList = self.count()

        if index == 0:
            self.insertAtFront(data)
        
        elif index == countList:
            self.insertAtEnd(data)
        
        elif index > countList:
            print("insertAtIndex: invalid index")
        
        elif index < countList:
            for i in range(index):
                pre_ptr = ptr
                ptr = ptr.next
            new_node.next = ptr
            pre_ptr.next = new_node



    def removeAtIndex(self, index):
    # Remove the node at a given index
        ptr = self.head
        pre_ptr = self.head
        countList = self.count()

        if index == 0:
            self.removeFront()

        if index == countList:
            self.removeEnd()

        if index > countList:
            print("removeAtIndex: Invalid index")
        
        if index < countList:
            for i in range(index):
                pre_ptr = ptr
                ptr = ptr.next
            pre_ptr.next = ptr.next
    