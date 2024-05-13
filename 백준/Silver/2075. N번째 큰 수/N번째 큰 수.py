import sys, heapq
input = sys.stdin.readline

n = int(input())
q = []

for _ in range(n):
    nums = list(map(int, input().split()))
    if not q: # 첫 번째 줄
        for num in nums:
            heapq.heappush(q, num)
    else:
        for num in nums:
            if q[0] < num:
                heapq.heappop(q)
                heapq.heappush(q, num)

print(q[0])