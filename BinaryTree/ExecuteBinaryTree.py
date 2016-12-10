from Tree import tree
from random import randint

def Process():
    print('Binary Tree')

    valueToFind = 0
    bTree = tree()
    for x in range(1, 11):
        number = randint(0,100)
        bTree.add(number)
        if x == 5:
            valueToFind = number

    bTree.printTree()

    result = bTree.findByValue(valueToFind)
    print('Value ' + str(valueToFind) + ' found: ' + str(result))

    print('end')