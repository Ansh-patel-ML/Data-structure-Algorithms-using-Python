def BinarySearch(arr, x):  # argument: (arr, x) --> arr = array, x = element we need to search
    start = 0  # where we need to start searching
    end = len(arr) - 1  # where we need to end searching

    while (start <= end):  # start index will be <= end index if start > end that means we cross end index and we
        # didn't find x
        mid = (start + end) // 2  # middle element of a list/array --> better start + (end - start) / 2

        if arr[mid] == x:  # if middle element == x (element we are searching) then return it's index
            return mid
        elif arr[mid] < x:  # if middle element is less then x then we will that element on right side of list
            start = mid + 1  # start searching after then middle element
        else:  # # if middle > x then we will found our element on left side so start index will remain same
            end = mid - 1  # our end index will be before our middle element
    return -1  # didn't find element return -1 (no element found)


arr = [1, 3, 4, 7, 9, 11, 23, 45]
index = BinarySearch(arr, 11)
print(index)
