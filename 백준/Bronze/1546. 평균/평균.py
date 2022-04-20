import sys

N = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().split()))
new_list = []

num_max = max(num_list)


for num in num_list:
  num = (num / num_max) * 100
  new_list.append(num)

print(sum(new_list)/N)