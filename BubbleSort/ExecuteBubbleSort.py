from BubbleSort import Bubble
from random import randint

def Process():
    print('Bubble sort')

    collection = [10]
    for x in range(1, 11):
        number = randint(0,100)
        collection.append(number)

    bubble = Bubble.BubbleSort(collection)

    print(bubble.printCollection(collection))
    result = bubble.sort()
    print(bubble.printCollection(result))
