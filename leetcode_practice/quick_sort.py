def quick_sort(collection):
    length = len(collection)
    if length <= 1:
        return collection
    else:
        pivot = collection[0]
        smaller = [element for element in collection[1:] if element <= pivot]
        larger = [element for element in collection[1:] if element >= pivot]
        return quick_sort(smaller) + [pivot] + quick_sort(larger)



