def bubble_sort(collection):
    length = len(collection)
    for i in range(length):
        swapped = False
        for j in range(length-1):
            if collection[j] > collection[j+1]:
                collection[j], collection[j+1] = collection[j+1], collection[j]
                swapped = True
        if not swapped:
           break
    return collection

if __name__  == "__main__":
    numlist = [1, 6, 5, 8, 9]
    numlist = bubble_sort(numlist)
    for i in range(len(numlist)):
        print(numlist[i])


