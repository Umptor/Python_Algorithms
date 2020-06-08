import math


def binarySearch(arr, element):
    return binarySearchAlgo(arr, element, 0, int(len(arr) - 1))


def binarySearchAlgo(arr, element, current_index, jump):

    if current_index < 0 or current_index >= len(arr):
        return -1
    if arr[current_index] == element:
        return current_index
    if jump < 1:
        return -1
    if element > arr[current_index]:
        if jump == 1:
            return binarySearchAlgo(arr, element, current_index + jump, 0)
        else:
            return binarySearchAlgo(arr, element, current_index + jump, math.ceil(jump / 2))
    else:
        if jump == 1:
            return binarySearchAlgo(arr, element, current_index - jump, 0)
        else:
            return binarySearchAlgo(arr, element, current_index - jump, math.ceil(jump / 2))


def binarySearchIter(arr, element):
    low = 0
    high = len(arr) - 1

    while low <= high:
        current_index = math.ceil((high + low) / 2)
        if arr[current_index] == element:
            return current_index
        if low == high:
            return -1
        if element > arr[current_index]:
            low += (high - low) / 2
        else:
            high -= (high - low) / 2


    return -1

f = open('Test Array.txt', 'r')
line = f.readline().split(" ")

for j in range(len(line)):
    line[j] = int(line[j])
# for j in line:
#     print(binarySearch(line, j))

for j in line:
    print(binarySearchIter(line, j))


# print(binarySearch(line, -1))