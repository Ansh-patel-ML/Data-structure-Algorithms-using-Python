def Fibonacci(n):
    if n == 1 or n == 2:  # base case of a recursion
        return 1
    fib_1 = Fibonacci(n - 1)  # recursion with smaller input
    fib_2 = Fibonacci(n - 2)  # recursion with smaller input

    return fib_1 + fib_2


print(Fibonacci(4))
