def firstindexb(li, si, x):
    l = len(li)

    if si == l:  # base case of a recursion
        return -1

    if x == li[si]:  # base case of a recursion
        return si

    smaller = firstindexb(li, si + 1, x)  # recursion with smaller input
    return smaller


li = [1, 9, 445, 7, 9]
output = firstindexb(li, 0, 9)
print(output)
