def power_recursion(n, x):
    if x == 0:  # base case of a recursion
        return 1
    return n ** power_recursion(n, x - 1)  # recursion with smaller input


y = power_recursion(2, 2)
print(y)
