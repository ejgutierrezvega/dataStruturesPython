
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setLeft(self, data):
        self.left = data

    def setRigth(self, data):
        self.right = data

    def getData(self):
        return str(self.data)

    def getLeftData(self):
        if self.left is None:
            return ''
        else:
            return '/' + str(self.left.data) + '(l)'

    def getRightData(self):
        if self.right is None:
            return ''
        else:
            return '/' + str(self.right.data) + '(r)'
