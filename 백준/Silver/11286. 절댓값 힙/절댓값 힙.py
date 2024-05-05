# 풀이 참고

import sys, heapq

input = sys.stdin.readline
heap = []

for _ in range(int(input())):
    x = int(input())
    if x == 0:
        if heap:
            val, sgn = heapq.heappop(heap)
            print(val*sgn)
        else:
            print(0)
    else:
        heapq.heappush(heap, [abs(x), x//abs(x)])
