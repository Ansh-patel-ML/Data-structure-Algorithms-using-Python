def merge(a1, a2, a):
    i = 0
    j = 0
    k = 0

    while i < len(a1) and j < len(a2):

        if a1[i] < a2[j]:
            a[k] = a1[i]
            i += 1
            k += 1
        else:
            a[k] = a2[j]
            j += 1
            k += 1
    while i < len(a1):
        a[k] = a1[i]
        i += 1
        k += 1
    while j < len(a2):
        a[k] = a2[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr

    mid = len(arr) // 2

    a1 = arr[0:mid]
    a2 = arr[mid:]

    merge_sort(a1)
    merge_sort(a2)

    merge(a1, a2, arr)


arr = [2, 4, 6, 9, 1, 4, 7, 9, 3, 6]
merge_sort(arr)
print(arr)
