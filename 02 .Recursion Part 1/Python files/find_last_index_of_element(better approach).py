def lastindexb(li, si, x):
    l = len(li)

    if si == l:  # base case of a recursion
        return -1

    smallerlist = lastindexb(li, si + 1, x)  # recursion with smaller input
    if smallerlist != -1:
        return smallerlist
    else:
        if li[si] == x:
            return si
        else:
            return -1


li = [1, 1, 445, 7, 9]
output = lastindexb(li, 0, 3)
print(output)
