# Original implementation
def merge_sorted_arrays(a, b):
    a_length = len(a)
    b_length = len(b)
    result = []

    while a or b:
        if not a:
            result.extend(b) # arr[len(arr):] = [x]
            b.clear()        # del arr[:]
        elif not b:
            result.extend(a)
            a.clear()
        elif a[0] < b[0]:
            result.append(a.pop(0))
        else:
            result.append(b.pop(0))
    
    return result

# Using built-ins...
def merge_sorted_arrays_alt(a, b):
    return sorted(a+b)

# with open('rosalind_mer.txt') as f:
with open('/Users/kleimkuhler/Downloads/rosalind_mer.txt') as f:
    lines = f.read().splitlines()
    a = [int(x) for x in lines[1].split(' ')]
    b = [int(x) for x in lines[3].split(' ')]

    print(' '.join(str(x) for x in merge_sorted_arrays(a, b)))
