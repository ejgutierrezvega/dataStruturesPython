from stack import Stack

def Process():
    stack = Stack()
    text = '(a[]{}([{}]d))'
    symbols = {'{': '}', '[': ']', '(': ')'}

    for x in text:
        found = findDictionaryByKey(symbols, x)
        if found:
            stack.push(x)
        else:
            foundByValue = findDictionaryByValue(symbols, x)
            if foundByValue:
                peekResult = stack.peek()
                if peekResult == foundByValue[0]:
                    stack.pop()

    if stack.is_empty():
        print('text is well format')
    else:
        print('text is not correctly format: ')
        stack.get_items()


def findDictionaryByKey(dictionary, key):
    for k, v in dictionary.items():
        if k == key:
            return k, v
    return None

def findDictionaryByValue(dictionary, value):
    for k, v in dictionary.items():
        if v == value:
            return k, v
    return None
