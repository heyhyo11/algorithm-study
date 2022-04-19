import sys

a, b = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
new_list = []

for i in range(a):
  if num_list[i] < b:
    new_list.append(num_list[i])

for j in range(len(new_list)):
  print(new_list[j], end=' ')