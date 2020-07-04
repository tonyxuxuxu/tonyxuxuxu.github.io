def merge_sort(collection):
    length = len(collection)
    if length > 1:
        midpoint = int(length/2)
        leftpart = merge_sort(collection[:midpoint])
        rightpart = merge_sort(collection[midpoint:])
        i = j = k = 0
        leftlength = len(leftpart)
        rightlength = len(rightpart)
        while i < leftlength and j < rightlength:
            if leftpart[i] < rightpart[j]:
                collection[k] = leftpart[i]
                k += 1
                i += 1
            else:
                collection[k] = rightpart[j]
                k += 1
                j += 1
        while i < leftlength:
            collection[k] = leftpart[i]
            k += 1
            i += 1
        while j < rightlength:
            collection[k] = rightpart[j]
            k += 1
            j += 1
    return collection

                
