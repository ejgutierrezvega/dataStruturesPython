
class BubbleSort(object):

    def __init__(self, data):
        self.data = data

    def sort(self):
        flag = True
        while flag:
            flag = False
            for index in range(len(self.data)-1):
                if self.data[index] >  self.data[index+1]:
                    temp = self.data[index]
                    self.data[index] = self.data[index+1]
                    self.data[index+1] = temp
                    flag = True
        return self.data

    def printCollection(self, input):
        chain = ''
        for element in input:
            chain += str(element) + ', '

        return chain

