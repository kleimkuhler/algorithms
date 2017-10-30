def insertion_sort(arr):
    count = 0
    length = len(arr)

    for i in range(1, length):
        while i > 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
            count += 1

    return count

# with open('rosalind_ins.txt') as f:
with open('/Users/kleimkuhler/Downloads/rosalind_ins.txt') as f:
    lines = f.read().splitlines()
    arr = [int(x) for x in lines[1].split(' ')]

    print('{} '.format(insertion_sort(arr), end=''))
