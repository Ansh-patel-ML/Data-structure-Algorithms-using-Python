def Binary_Search(a, x, si, ei):
    if si > ei:
        return -1

    mid = (si + ei) // 2

    if a[mid] == x:
        return mid
    elif a[mid] > x:
        return Binary_Search(a, x, si, mid - 1)
    else:
        return Binary_Search(a, x, mid + 1, ei)


a = [1, 2, 3, 55, 67, 89, 100]
print(Binary_Search(a, 100, 0, len(a) - 1))