class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def getData(self):
        return self.data

    def getNext(self):
        return self.next_node

    def setNext(self, newdata):
        self.next_node = newdata