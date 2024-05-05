import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    items = {}
    ans = 1
    for _ in range(m):
        name, item = input().split()
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
    for i in items.values():
        ans *= (int(i)+1)
    print(ans-1)