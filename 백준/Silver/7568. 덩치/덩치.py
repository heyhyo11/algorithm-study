import sys

# 기본 세팅
N = int(sys.stdin.readline())
N_list = []
cnt_list = []

# x, y 입력받아서 N_list 안에 넣기
for _ in range(N):
  x, y = map(int, sys.stdin.readline().rstrip().split())
  N_list.append([x, y])

# 리스트를 돌면서 i번째 요소와 모든 요소를 하나씩 비교함
for i in N_list:
  cnt = 1
  for j in N_list:
    if i == j:
      continue
    else:
      if i[0] < j[0] and i[1] < j[1]:
        cnt += 1
  cnt_list.append(cnt)
  
# 정답 출력
print(*cnt_list)