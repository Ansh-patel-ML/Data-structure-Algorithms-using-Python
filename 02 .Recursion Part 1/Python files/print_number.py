def print_num(n):
    if n == 0:  # base case of a recursion
        return 0
    print_num(n - 1)  # recursion with smaller input
    print(n)


print_num(5)

