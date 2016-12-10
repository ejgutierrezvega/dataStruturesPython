from Node import Node

class LinkedList(object):
    size = 0

    def __init__(self, head=None):
        self.head = head

    def Add(self, data):
        self.size += 1
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node

    def AddLast(self, data):
        self.size += 1
        new_node = Node(data)
        if (self.head == None):
            new_node.setNext(self.head)
            self.head = new_node
        else:
            current = self.head
            while(current.next_node != None):
                current = current.next_node

            current.next_node = new_node

    def Count(self):
        return self.size

    def GetAllValues(self):
        current = self.head
        while (current.next_node != None):
            print(current.getData())
            current = current.next_node

        print(current.getData())

    def FindByPosition(self, position, reverse):
        if (reverse == 'true'):
            position = self.size - (position-1)

        current = self.head
        index = 1
        while(current.next_node != None):
            if (position == index):
                return current.getData()
            current = current.next_node
            index += 1