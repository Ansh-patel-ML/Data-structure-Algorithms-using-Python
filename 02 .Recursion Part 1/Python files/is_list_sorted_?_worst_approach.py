def issorted(li):
    length = len(li)

    if length == 0 or length == 1:  # base case of a recursion
        return True
    if li[0] > li[1]:  # base case of a recursion
        return False
    smallerlist = li[1:]  # this is worst because it's making copy every time we call with smaller input
    smallerlistoutput = issorted(smallerlist)  # recursion with smaller input
    return smallerlistoutput


li = [1, 2]
output = issorted(li)
print(output)
