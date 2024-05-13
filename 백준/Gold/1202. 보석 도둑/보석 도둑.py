# 풀이 참고

import sys, heapq
input = sys.stdin.readline


n, k = map(int, input().split())
jewerly = []

for i in range(n):
    m, v = map(int, input().split())
    heapq.heappush(jewerly, (m, v)) # 최소힙

bags = [int(input()) for _ in range(k)]
bags.sort()

ans = 0
temp = []

for bag in bags:
    while jewerly and bag >= jewerly[0][0]: # 가방에 보석 넣을 수 있나
        heapq.heappush(temp, -heapq.heappop(jewerly)[1]) # 최대힙
    if temp:
        ans -= heapq.heappop(temp)
    elif not jewerly:
        break

print(ans)