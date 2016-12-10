from Node import Node

class LinkedList(object):
    size = 0

    def __init__(self, head=None):
        self.head = head

    def add(self, data):
        self.size += 1
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node

    def addLast(self, data):
        self.size += 1
        new_node = Node(data)
        if self.head is None:
            new_node.setNext(self.head)
            self.head = new_node
        else:
            current = self.head
            next_node = current.getNext()
            while next_node is not None:
                current = next_node
                next_node = current.getNext()

            current.setNext(new_node)

    def count(self):
        return self.size

    def getAllValues(self):
        result = ''
        current = self.head
        while current.getNext() is not None:
            result += str(current.getData()) + ', '
            current = current.getNext()

        result += str(current.getData()) + ', '
        print(result)

    def findByPosition(self, position, reverse):
        if reverse is True:
            position = self.size - (position-1)

        current = self.head
        index = 1
        while current.getNext() is not None:
            if position == index:
                return current.getData()
            current = current.getNext()
            index += 1

    def findByValue(self, value):
        current = self.head
        while current.getNext() is not None:
            if current.getData() == value:
                return current.getData()
            current = current.getNext()

    def deleteByValue(self, value):
        current = self.head
        previous = None
        found = False
        while current.getNext() is not None and found is False:
            if current.getData() == value:
                previous.setNext(current.getNext())
                found = True

            previous = current
            current = current.getNext()

    def addValueAfter(self, value, data):
        new_value = Node(value)
        current = self.head
        inserted = False
        while current.getNext() is not None and inserted is False:
            if current.getData() == data:
                new_value.setNext(current.getNext())
                current.setNext(new_value)
                inserted = True
            current = current.getNext()