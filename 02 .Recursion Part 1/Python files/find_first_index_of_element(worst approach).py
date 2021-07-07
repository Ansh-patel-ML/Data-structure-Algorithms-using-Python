def firstindex(li, x):
    l = len(li)
    if l == 0:  # base case of a recursion
        return -1

    if li[0] == x:  # base case of a recursion
        return 0

    copy = li[1:]

    smallercopy = firstindex(copy, x)  # recursion with smaller input
    if smallercopy == -1:
        return -1
    else:
        return smallercopy + 1


li = [0, 2, 1, 4, 2, 6, 8, 0, 11, 3, 1, 4]
output = firstindex(li, 1)
print(output)