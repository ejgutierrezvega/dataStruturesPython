
def Process():
    items = []
    number = 0
    index = 0

    items.append(number)
    for element in range(0, 15):
        if index > 0:
            number = number + items[index - 1]
        else:
            number = 1

        index += 1

        items.append(number)

    result = ''
    for item in items:
        result += str(item) + ','

    print result