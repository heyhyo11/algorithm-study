import sys

input = sys.stdin.readline
arr = list(input())

for i in range(len(arr)):
    max_value = i
    for j in range(i+1, len(arr)):
        if arr[j] > arr[max_value]:
            max_value = j
    if arr[i] < arr[max_value]:
        arr[i], arr[max_value] = arr[max_value], arr[i]

print(''.join(arr))