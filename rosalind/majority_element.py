def majority_element(arr):
    elements = {}
    length = len(arr)

    for i in range(0, length):
        key = arr[i]

        if key in elements:
            elements[key] += 1

            if elements[key] > length/2:
                return key
        else:
            elements[key] = 1

    return -1
        

# with open('rosalind_maj.txt') as f:
with open('/home/kleimkuhler/Downloads/rosalind_maj.txt') as f:
    lines = f.read().splitlines()
    lines.pop(0)  # don't need first line of input

    for line in lines:
        print('{} '.format(majority_element([int(x) for x in line.split(' ')])), end='')

    print()
