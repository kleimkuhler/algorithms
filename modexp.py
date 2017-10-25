# Recursive modular artithmetic implementation of exponential
def modexp(x, y, N):
    if y == 0:
        return 1
    z = modexp(x, y//2, N)
    if y % 2 == 0:
        return pow(z, 2) % N
    else:
        return x * pow(z, 2) % N
