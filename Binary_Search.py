def binary_search(array, value):

    first = 0
    last = len(array) - 1

    found = False

    while first <= last and not found:

        mid = (first + last) // 2

        if array[mid] == value:
            found = True
        else:
            if value < array[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


arr = list(range(0, 11))

print(binary_search(arr, 5))
