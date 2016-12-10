from Tree import tree
from random import randint

def Process():
    print('Binary Tree')

    valueToFind = 0
    bTree = tree()

    numbers = ''
    for x in range(1, 11):
        number = randint(0,100)
        numbers += str(number) + ','
        bTree.add(number)
        if x == 5:
            valueToFind = number

    print('Numbers: ' + numbers)

    '''
    collection = [23, 13, 36, 17, 25, 90, 29, 88, 71, 49]
    for x in collection:
        bTree.add(x)
    valueToFind = 36
    '''

    bTree.printTree()

    print('Tree size: ' + str(bTree.count()))

    result = bTree.findByValue(valueToFind)
    print('Value ' + str(valueToFind) + ' found: ' + str(result))

    result = bTree.findMin()
    print('Min value: ' + str(result))

    print('Breadth first')
    bTree.findByValueBreadthFirst(valueToFind)

    print('Value to remove: ' + str(valueToFind))
    result = bTree.removeByValue(valueToFind)
    if result:
        print('Value removed')

    result = bTree.removeMin()
    print('Min value removed: ' + str(result))

    print('Tree size: ' + str(bTree.count()))
    bTree.printTree()
