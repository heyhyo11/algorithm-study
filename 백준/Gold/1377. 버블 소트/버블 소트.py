import sys

input = sys.stdin.readline
n = int(input())
a = []

for i in range(n):
    a.append((int(input()), i))
             
max_value = 0
a.sort()
             
for i in range(n):
    if max_value < a[i][1] - i:
        max_value = a[i][1] - i
             
print(max_value + 1)