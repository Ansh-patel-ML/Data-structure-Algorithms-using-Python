def sumofnumbers(n):  # argument: (n) --> number
    if n == 0:  # base case of a recursion
        return 0
    return n + sumofnumbers(n - 1)  # recursion with smaller input


x = sumofnumbers(3)
print(x)
