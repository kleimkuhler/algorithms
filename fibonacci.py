# Implementation using a helper function
def fib_helper(n, a, b):
    if n != 0:
        return fib_helper(n-1, b, a+b)
    return a

def fib1(n):
    print(fib_helper(n, 0, 1))

# Implementation without helper function
# This one is obviously a lot cleaner because, unlike scheme, I now remember
# loops are thing ^_^
def fib2(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, b+a
    return a
