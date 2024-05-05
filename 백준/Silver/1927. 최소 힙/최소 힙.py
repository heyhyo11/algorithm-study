import sys, heapq

input = sys.stdin.readline

n = int(input())
heap_items = []

for _ in range(n):
    item = int(input())
    if item == 0:
        try:
            print(heapq.heappop(heap_items))
        except:
            print(0)
    else:
        heapq.heappush(heap_items, item)