def lastindex(li, x):
    l = len(li)

    if l == 0:  # base case of a recursion
        return -1

    copy = li[1:]
    smallerlist = lastindex(copy, x)  # recursion with smaller input

    if smallerlist != -1:
        return smallerlist + 1
    else:
        if li[0] == x:
            return 0
        else:
            return -1


li = [1, 1, 445, 7, 9]
output = lastindex(li, 1)
print(output)
