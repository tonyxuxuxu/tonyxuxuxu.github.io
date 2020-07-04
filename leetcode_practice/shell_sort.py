def shell_sort(collection):
    length = len(collection)
    gap = int(length/2) 
    while gap > 0:
        for i in range(gap, length):
            j = i
            while j >= gap and collection[j-gap] > collection[j]:
                collection[j-gap], collection[j] = collection[j], collection[j-gap]
            j -= gap
        gap = int(gap/2)
    return collection
            

