def merge_sort(arr):
    length_arr = len(arr)

    # Base case of array size == 0 or 1
    if length_arr <= 1:
        return arr

    left = []
    right = []
    for i in range(0, length_arr):
        if i < length_arr // 2:
            left.append(arr[i])
        else:
            right.append(arr[i])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

# merge taken from merge_sorted_arrays solution
def merge(a, b):
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

# with open('rosalind_ms.txt') as f:
with open('/home/kleimkuhler/Downloads/rosalind_ms.txt') as f:
    lines = f.read().splitlines()
    arr = [int(x) for x in lines[1].split(' ')]

    print(' '.join(str(x) for x in merge_sort(arr)))
