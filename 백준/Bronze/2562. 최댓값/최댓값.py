import sys

num_list = []


for _ in range(9):
  num = int(sys.stdin.readline())
  num_list.append(num)

print(max(num_list), num_list.index(max(num_list))+1)