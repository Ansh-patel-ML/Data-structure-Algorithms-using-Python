def Partison(arr, si, ei):
    pivot = arr[si]
    c = 0
    for i in range(si, ei + 1):
        if arr[i] < pivot:
            c += 1

    arr[si + c], arr[si] = arr[si], arr[si + c]
    pivot_index = si + c
    i = si
    j = ei

    while i < j:
        if arr[i] < pivot:
            i = i + 1
        elif arr[j] >= pivot:
            j = j - 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return pivot_index


def QuickSort(arr, si, ei):
    if si >= ei:
        return

    pivot_index = Partison(arr, si, ei)

    QuickSort(arr, si, pivot_index - 1)
    QuickSort(arr, pivot_index + 1, ei)


arr = [2, 4, 1, 0, 8, 3]
QuickSort(arr, 0, len(arr) - 1)
print(arr)
