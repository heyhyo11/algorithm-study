from itertools import combinations
import sys

# 1. 데이터 입력 받기
n, m = map(int, sys.stdin.readline().split())
graph = []
chicken = []
city = []

for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))
  

# 2. graph에서 1, 2가 있는 좌표 찾기
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      city.append([i, j])
    elif graph[i][j] == 2:
      chicken.append([i, j])

      
# 3. combination을 이용하여 치킨집의 모든 경우의 수를 구한 뒤, 최소거리 비교하기
result = 99999
for i in combinations(chicken, m):
  temp = 0 # 도시 치킨 최소 거리
  for house in city:
    chicken_dist = 999
    for j in range(m):
      chicken_dist = min(chicken_dist, abs(house[0]-i[j][0]) + abs(house[1]-i[j][1]))
    temp += chicken_dist
  result = min(result, temp)

print(result)