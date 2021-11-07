def Assending_Binary_Search(arr, x, start, end):
    while start <= end:
        mid_element = int(start + (end - start) / 2)
        if arr[mid_element] == x:
            return mid_element
        elif x < arr[mid_element]:
            end = mid_element - 1
        else:
            start = mid_element + 1
    return -1


def Decending_Binary_Search(arr, x, start, end):
    while start <= end:
        mid_element = int(start + (end - start) / 2)
        if arr[mid_element] == x:
            return mid_element
        elif x < arr[mid_element]:
            start = mid_element + 1
        else:
            end = mid_element - 1
    return -1


def Binary_Search(arr, x):
    start = 0
    end = len(arr) - 1

    if arr[start] < arr[end]:
        return Assending_Binary_Search(arr, x, start, end)
    else:
        return Decending_Binary_Search(arr, x, start, end)


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 11
print(Binary_Search(array, target))
