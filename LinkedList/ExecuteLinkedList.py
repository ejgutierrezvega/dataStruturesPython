from LinkedList import Linkedlist

def Process():
    print('Linked list')

    list = Linkedlist.LinkedList()
    for x in range(1, 11):
        list.addLast(x)

    size = list.count()
    print('Size:' + str(size))

    list.getAllValues()

    result = list.findByPosition(3, False)
    print('Position: ' + str(result))

    result = list.findByPosition(3, True)
    print('Position: ' + str(result))

    result = list.findByValue(14)
    print('Value found: ' + str(result))

    print('Delete value')
    list.deleteByValue(7)

    print('Add value after')
    list.addValueAfter(50, 4)

    list.getAllValues()