import linkedlist

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
    assert num == 0, f"count() expected 1, got {num}"

    a = linkedlist()
    for i in range(10):
        a.insertAtFront(i)
    num  = a.count()
    assert num == 0, f"count() expected 10, got {num}"
    
if __name__ == "__main__":
    test_init()
    test_isEmpty()
    test_insertAtFront()
    test_isEmpty2()
    test_count()