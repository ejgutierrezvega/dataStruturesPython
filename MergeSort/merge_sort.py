
def _mergesort(items):
    if len(items) > 1:
        mid = len(items)/2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        _mergesort(lefthalf)
        _mergesort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                items[k] = lefthalf[i]
                i += 1
            else:
                items[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            items[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            items[k] = righthalf[j]
            j += 1
            k += 1

    return items

def Process():
    collection = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(collection)
    merge_collection = _mergesort(collection)
    print(merge_collection)
