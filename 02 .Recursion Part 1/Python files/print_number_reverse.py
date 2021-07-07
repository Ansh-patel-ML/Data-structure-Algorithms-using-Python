def print_rev(n):
    if n == 0: # base case of a recursion
        return 0
    print(n)
    print_rev(n-1) # recursion with smaller input


print_rev(5)