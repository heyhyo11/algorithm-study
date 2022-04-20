import sys

str_list = sys.stdin.readline().rstrip()
alpha_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt_list = []

for alpha in alpha_list:
  cnt = str_list.count(alpha)
  cnt_list.append(cnt)
  
cnt_list[7] -= cnt_list[2]
others = len(str_list) - sum(cnt_list)*2 - cnt_list[2]

# ans = other + sum(cnt_list) 이거 풀어쓴 것
ans = len(str_list) - sum(cnt_list) - cnt_list[2]
print(ans)