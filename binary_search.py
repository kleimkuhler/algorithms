# Binary search that has no recursive calls that I like
def binary_search(m, arr):
    lo = 0
    hi = len(arr)

    result = -1
    while lo < hi:
        pos = (lo+hi)//2
        if m == arr[pos]:
            return pos+1
        elif m < arr[pos]:
            hi = pos
        else:
            lo = pos+1

    return result
    
# with open('rosalind_bins.txt') as f:
with open('/Users/kleimkuhler/Downloads/rosalind_bins.txt') as f:
    lines = f.read().splitlines()
    n = int(lines[0])
    m = int(lines[1])
    arr_n = [int(x) for x in lines[2].split(' ')]
    arr_m = [int(x) for x in lines[3].split(' ')]

    for i in range(0, m):
        print('{} '.format(binary_search(arr_m[i], arr_n)), end='')

    # Newline copy/pasting purposes ^_^
    print()
