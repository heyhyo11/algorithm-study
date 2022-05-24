import sys

T = int(sys.stdin.readline())

case_list = [1, 1, 1, 2, 2]
cnt = 5

while len(case_list) < 101:
  case_list.append(case_list[cnt-5] + case_list[cnt-1])
  cnt += 1


for _ in range(T):
  N = int(sys.stdin.readline())
  print(case_list[N-1])