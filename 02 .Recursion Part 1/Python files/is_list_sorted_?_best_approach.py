def issortedb(li, index):
    length = len(li)

    if index == length - 1 or length == index:  # base case of a recursion
        return True
    if li[index] > li[index + 1]:  # base case of a recursion
        return False

    smallerlistoutput = issortedb(li, index + 1)  # recursion with smaller input
    return smallerlistoutput


li = [1, 2, 3, 4, 67, 2]
output = issortedb(li, 0)
print(output)
