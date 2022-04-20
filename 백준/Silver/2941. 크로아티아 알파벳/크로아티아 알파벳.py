import sys

str_list = sys.stdin.readline().rstrip()
alpha_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alpha_list:
  str_list = str_list.replace(i, "*")

print(len(str_list))