# Recycling my answer from merge_sort instead of using built-in because RRR
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

def two_sum(arr):
    sorted_arr = merge_sort(arr)

    for index, item in enumerate(arr):
        sum_index = binary_search(-item, sorted_arr)

        if sum_index != -1:
            return [index+1, arr.index(-item)+1]

    return -1

# with open('rosalind_.txt') as f:
with open('/home/kleimkuhler/Downloads/rosalind_.txt') as f:
    lines = f.read().splitlines()
    lines.pop(0)  # don't need first line of input

    for line in lines:
        print('{}'.format(two_sum([int(x) for x in line.split(' ')])))

    print()
