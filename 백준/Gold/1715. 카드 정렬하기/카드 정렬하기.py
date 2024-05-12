import sys, heapq
input = sys.stdin.readline

n = int(input())
cards = [int(input()) for _ in range(n)]
heapq.heapify(cards)
ans = 0

while len(cards) > 1:
    small_1 = heapq.heappop(cards)
    small_2 = heapq.heappop(cards)
    temp = small_1 + small_2
    ans += temp
    heapq.heappush(cards, temp)

print(ans)