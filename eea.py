# Extended euclidean algorithm for finding ax + by = d
# (x, y) are used in finding the modular multiplicative inverse
def eea(x, y):
    if y == 0:
        return [1, 0, x]
    z = eea(y, x%y)
    return (z[1], z[0]-x//y*z[1], z[2])
