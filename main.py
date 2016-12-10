from LinkedList import ExecuteLinkedList
from BinaryTree import ExecuteBinaryTree
from BubbleSort import ExecuteBubbleSort
from Stack import ExecuteStack

def get_options():
    options = {
        '0': 'Exit',
        '1': 'Linked list',
        '2': 'Binary tree',
        '3': 'Bubble sort',
        '4': 'Stack'
    }

    return options

def print_options(options):
    for k, v in sorted(options.items()):
        print(k + ':' + v)

    return int(input('Choose option: '))

def execute_option(option):
    result = True
    if option == 1:
        ExecuteLinkedList.Process()
    elif option == 2:
        ExecuteBinaryTree.Process()
    elif option == 3:
        ExecuteBubbleSort.Process()
    elif option == 4:
        ExecuteStack.Process()
    else:
        result = False
    return result

options = get_options()
result = True
while result:
    option = print_options(options)
    result = execute_option(option)
    print('--------------------------------------')
    print('')
