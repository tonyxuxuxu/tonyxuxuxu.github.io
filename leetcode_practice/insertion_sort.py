def insertion_sort(collection):
    length = len(collection)
    for i in range(length):
        while i > 0 and collection[i-1] > collection[i]:
            collection[i-1], collection[i] = collection[i], collection[i-1]
            i -= 1
    return collection


