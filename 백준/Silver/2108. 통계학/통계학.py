import sys
from collections import Counter

N = int(sys.stdin.readline().rstrip())
num_list = []

for _ in range(N):
  n = int(sys.stdin.readline().rstrip())
  num_list.append(n)
  
num_list.sort()
  
# 산술평균, 중간값, 범위 구하기  
print(round(sum(num_list)/N))
print(num_list[(N//2)])


# 최빈값 구하기
# 풀이 2. Counter 라이브러리 이용
mode_list = Counter(num_list).most_common(2)
if len(mode_list) > 1:
  if mode_list[0][1] == mode_list[1][1]:
    print(mode_list[1][0])
  else:
    print(mode_list[0][0])
else:
    print(mode_list[0][0])


# 풀이 1. 시간초과
# if len(num_list) == 1:
#   print(num_list[0])
# else:
#   mode_list = [0] * (num_list[-1]-num_list[0]+1)
#   for i in num_list:
#     mode_list[i+abs(min(num_list))] += 1
#   # 최빈값 중 두 번째로 작은 값 출력
#   mode_list.remove(max(mode_list))
#   print(mode_list.index(max(mode_list)) + min(num_list) + 1)

# 범위 출력
print(num_list[-1] - num_list[0])