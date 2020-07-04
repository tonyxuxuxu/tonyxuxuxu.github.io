def selection_sort(collection):
    length = len(collection)
    for i in range(length):
        least = i
        for j in range(i+1, length):
            if collection[j] < collection[i]:
                least = j
        collection[i], collection[least] = collection[least], collection[i]
    return collection

