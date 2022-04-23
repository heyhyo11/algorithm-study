import sys

# 1. 입력 받기
x_cnt_list = []
y_cnt_list = []

# 2. x, y를 각각 리스트에 추가하기
for i in range(3):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  x_cnt_list.append(x)
  y_cnt_list.append(y)

# 3. x, y 좌표 구하기
for i in x_cnt_list:
  if x_cnt_list.count(i) == 1:
    x_ans = i
    break

for i in y_cnt_list:
  if y_cnt_list.count(i) == 1:
    y_ans = i
    break

print(x_ans, y_ans)