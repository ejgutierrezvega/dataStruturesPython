from Node import Node
from QueueStructure import queue_struct

class tree(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def getRoot(self):
        return self.root

    def count(self):
        return self.size

    def add(self, val):
        self.size += 1
        node = Node(val)
        if self.root is None:
            self.root = node
        else:
            self._add(node, self.root)

    def _add(self, val, node):
        if val.data < node.data:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.setLeft(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.setRigth(val)

    def findByValue(self, value):
        if self.root is not None:
            result = self._findByValue(value, self.root)
            if result is not None:
                return result.data
            else:
                return None
        else:
            return None

    def _findByValue(self, value, node):
        if value == node.data:
            return node
        elif value < node.data and node.left is not None:
            return self._findByValue(value, node.left)
        elif value > node.data and node.right is not None:
            return self._findByValue(value, node.right)

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
        else:
            return None

    def _printTree(self, node):
        if node is not None:
            print(node.getData() + node.getLeftData() + node.getRightData())
            if node.left is not None:
                self._printTree(node.left)
            if node.right is not None:
                self._printTree(node.right)

    def removeMin(self):
        self.size -= 1
        if self.root is not None:
            return self._removeMin(None, self.root)
        else:
            return None

    def _removeMin(self, head, node):
         if node.left is not None:
             left = self._removeMin(node, node.left)
             return left
         else:
             if node.right is not None:
                 head.left = node.right
             else:
                 head.left = None
             return node.data

    def findMin(self):
        if self.root is not None:
            return self._findMin(self.root)
        else:
            return None

    def _findMin(self, node):
        if node.left is not None:
            left = self._findMin(node.left)
            return left
        else:
            return node.data

    def removeByValue(self, val):
        self.size -= 1
        if self.root is not None:
            self._removeByValue(self.root, val)
            return True
        else:
            return False

    def _removeByValue(self, node, value):
        if value == node.data:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self._findMin(node.right)
            node.data = temp
            node.right = self._removeByValue(node.right, value)
        elif value < node.data and node.left is not None:
            node.left = self._removeByValue(node.left, value)
        elif value > node.data and node.right is not None:
            node.right = self._removeByValue(node.right, value)

        return node

    def findByValueBreadthFirst(self, value):
        result = ''
        if self.root is not None:
            q = queue_struct.queue_class()
            q.enqueue(self.root)
            while q.size() > 0:
                n = q.dequeue()
                result += n.getData() + ', '
                if n.getData() == str(value):
                    print result
                    return

                if n.left is not None:
                    q.enqueue(n.left)
                if n.right is not None:
                    q.enqueue(n.right)

        print result