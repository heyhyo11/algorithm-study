import sys

str_list = list(sys.stdin.readline().rstrip().upper())
set_list = list(set(str_list))
cnt_list = [0 for i in range(len(set_list))]

for i in range(len(set_list)):
  cnt_list[i] = str_list.count(set_list[i])

max_ = max(cnt_list)

if len(list(filter(lambda x: x == max_, cnt_list))) > 1:
  print("?")
else:
  print(set_list[cnt_list.index(max_)])