from Node import Node

class tree(object):
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
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
            self._printTree(node.right)
            print(str(node.data) + ' ')
            self._printTree(node.left)