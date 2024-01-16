from linkedlist import *

def test_init():
    a = linkedlist()
    assert a.head == None, "Linked list head not initialized to null"

def test_isEmpty():
    a = linkedlist()
    assert a.isEmpty(), "isEmpty() returned false on an empty linked list"

def test_insertAtFront():
    a = linkedlist()
    a.insertAtFront(1)
    assert a.head != None, "insertAtFront() did not insert any node"
    assert a.head.data == 1, f"insertAtFront() did not add correct data, expected 1, got {a.head.data}"
    assert a.head.next == None, "insertAtFront() did not set up "
def test_isEmpty2():
    a = linkedlist()
    a.insertAtFront(1)
    assert not a.isEmpty(), "isEmpty() returned true on a non-empty linked list"

def test_count():
    a = linkedlist()
    num  = a.count()
    assert num == 0, f"count() expected 0, got {num}"
    
    a.insertAtFront(1)
    num  = a.count()
    assert num == 1, f"count() expected 1, got {num}"

    a = linkedlist()
    for i in range(10):
        a.insertAtFront(i)
    num  = a.count()
    assert num == 10, f"count() expected 10, got {num}"
    
def test_get():
    a = linkedlist()
    for i in range(10):
        a.insertAtFront(i)
    num = a.getData(0)
    assert num == 0, f"getData() did not return correct data, expected 0, got {num}"
    num = a.getData(4)
    assert num == 4, f"getData() did not return correct data, expected 4, got {num}"
    num = a.getData(9)
    assert num == 9, f"getData() did not return correct data, expected 9, got {num}"

def test_update():
    a = linkedlist()
    for i in range(3):
        a.insertAtFront(i)
    a.updateNode(3,0)
    a.updateNode(4,1)
    a.updateNode(5,2)
    assert a.getData(0) == 3, "updateNode() did not update first node correctly"
    assert a.getData(0) == 4, "updateNode() did not update middle node correctly"
    assert a.getData(0) == 5, "updateNode() did not update last node correctly"

def test_removeFront():
    a = linkedlist()
    a.insertAtFront(1)
    a.removeFront()
    assert a.isEmpty(), "removeFront() did not remove correctly"
    for i in range(2):
        a.insertAtFront(i)
    a.removeFront()
    assert a.getData(0) == 0, "removeFront() did not remove correctly"

def test_insertAtEnd():
    a = linkedlist()
    for i in range(3):
        a.insertAtEnd(i)
    print("Your list")
    a.printLL()  
    print("Correct list\n [0, 1, 2]")

def test_removeEnd():
    a = linkedlist()
    a.insertAtFront(1)
    a.removeFront()
    assert a.isEmpty(), "removeEnd() did not remove correctly"

    a = linkedlist()
    for i in range(3):
        a.insertAtEnd(i)
    a.removeEnd()
    print("Your list")
    a.printLL()  
    print("Correct list\n [0, 1]")

def test_insertAtIndex():
    a = linkedlist()
    for i in range(4):
        a.insertAtEnd(i)
    a.insertAtIndex('a', 0)
    a.insertAtIndex('b', 3)
    a.insertAtIndex('c', 6)
    print("Your list")
    a.printLL()  
    print("Correct list\n ['a', 0, 1, 'b', 2, 3, 'c']")


def test_removeAtIndex():
    a = linkedlist()
    for i in range(5):
        a.insertAtEnd(i)
    a.removeAtIndex(4)
    a.removeAtIndex(2)
    a.removeAtIndex(0)
    print("Your list")
    a.printLL()  
    print("Correct list\n [1, 3]")


if __name__ == "__main__":
    test_init()
    test_isEmpty()
    test_insertAtFront()
    test_isEmpty2()
    test_count()
<<<<<<< HEAD
    test_get()
    test_update()
    test_removeFront()
    test_insertAtEnd()
    test_removeEnd()
    test_insertAtIndex()
    test_removeAtIndex()
    print("Congrats! You passed all the tests:)")