from LinkedList import Linkedlist

list = Linkedlist.LinkedList()
for x in range(1, 11):
    list.AddLast(x)

size = list.Count()
print('Size:' + str(size))

list.GetAllValues()

result = list.FindByPosition(3, 'false')
print('Position: ' + str(result))

result = list.FindByPosition(3, 'true')
print('Position: ' + str(result))