import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
minheap = []
maxheap = []
solved = defaultdict(int)

for i in range(n):
    p, l = map(int, input().split())
    heapq.heappush(minheap, (l, p)) # 최소힙
    heapq.heappush(maxheap, (-l, -p)) # 최대힙

m = int(input())

for _ in range(m):
    command = list(input().split())

    if command[0] == 'recommend':
        if command[1] == '1':
            while solved[abs(maxheap[0][1])] != 0:
                solved[abs(maxheap[0][1])] -= 1
                heapq.heappop(maxheap)
            print(-maxheap[0][1])

        elif command[1] == '-1':
            while solved[abs(minheap[0][1])] != 0:
                solved[minheap[0][1]] -= 1
                heapq.heappop(minheap)
            print(minheap[0][1])

    elif command[0] == 'add':
        p, l = int(command[1]), int(command[2])
        heapq.heappush(minheap, (l, p))
        heapq.heappush(maxheap, (-l, -p))

    elif command[0] == 'solved':
        solved[int(command[1])] += 1