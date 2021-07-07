def factorial(num):  # argument: (num) --> number
    if num == 0:  # base case of a recursion
        return 1
    return num * factorial(num - 1)  # recursion with smaller input


print(factorial(4))
