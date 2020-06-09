import math


def binary_sort(arr):
    return binary_sort_algo(arr, 0, len(arr) - 1)


def binary_sort_algo(arr, start, end):
    if start >= end:
        return

    binary_sort_algo(arr, start, math.floor((start + end) / 2))
    binary_sort_algo(arr, math.ceil((start + end) / 2), end)
    binary_sort_merge(arr, start, end)
    return arr


def binary_sort_merge(arr, start, end):
    new_arr = []
    middle = math.ceil((start + end) / 2)
    pnt1 = start
    pnt2 = middle

    while pnt1 < middle and pnt2 <= end:
        if arr[pnt1] < arr[pnt2]:
            new_arr.append(arr[pnt1])
            pnt1 += 1
        else:
            new_arr.append(arr[pnt2])
            pnt2 += 1

    while pnt1 < middle:
        new_arr.append(arr[pnt1])
        pnt1 += 1
    while pnt2 <= end:
        new_arr.append(arr[pnt2])
        pnt2 += 1

    for i in range(start, end + 1):
        arr[i] = new_arr[i - start]

    return arr


f = open('Binary Sort Text.txt', 'r')
line = []

for num in f.readline().split(" "):
    line.append(int(num))

print(binary_sort(line))